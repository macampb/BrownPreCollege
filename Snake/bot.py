import random
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
import snake_game

# --------------------------- Config --------------------------- #
N_EPISODES = 500
LR = 0.001
MEMORY = []
BLANK_LINES_BEFORE_DEMO = 15

EPSILON = 1.0
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.1
BATCH_SIZE = 64

EARLY_STOP_PATIENCE = 5   # checks without improvement
CHECK_INTERVAL = 50       # episodes
improvement_threshold = 0.01

# --------------------------- Model --------------------------- #
def create_model(input_dim, output_dim):
    model = models.Sequential([
        layers.Input(shape=(input_dim,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(output_dim)  # 4 Q-values: UP, DOWN, LEFT, RIGHT
    ])
    model.compile(optimizer=optimizers.Adam(LR), loss='mse')
    return model

# Encode state for training
def encode_state(state):
    head_x, head_y = state["snake"][0]
    food_x, food_y = state["food"]
    return np.array([head_x, head_y, food_x, food_y], dtype=np.float32)

# --------------------------- Bot --------------------------- #
class SnakeBotRL:
    DIRECTIONS = ("UP", "DOWN", "LEFT", "RIGHT")

    def next_move(self, state):
        head_x, head_y = state["snake"][0]
        food_x, food_y = state["food"]

        if head_x < food_x:
            return "RIGHT"
        elif head_x > food_x:
            return "LEFT"
        elif head_y < food_y:
            return "DOWN"
        else:
            return "UP"

    def __init__(self, model):
        self.model = model
        self.epsilon = EPSILON

    def next_move(self, state):
        if np.random.rand() < self.epsilon or len(MEMORY) < 50:
            return random.choice(self.DIRECTIONS)
        s = encode_state(state).reshape(1, -1)
        q_values = self.model.predict(s, verbose=0)
        return self.DIRECTIONS[np.argmax(q_values[0])]

    def decay_epsilon(self):
        self.epsilon = max(EPSILON_MIN, self.epsilon * EPSILON_DECAY)

# --------------------------- Train & Demo --------------------------- #
def train_and_demo():
    model = create_model(4, 4)
    bot = SnakeBotRL(model)

    scores = []
    best_avg = -float("inf")
    patience_counter = 0

    print(f"\nRunning {N_EPISODES} episodes…")

    for ep in range(1, N_EPISODES + 1):
        res, trajectory = run_and_collect(bot)
        scores.append(res["composite"])
        bot.decay_epsilon()

        # Train after each episode
        if trajectory:
            train_on_trajectory(model, trajectory)

        print(f"Episode {ep:3d}: score={res['score']} comp={res['composite']} ε={bot.epsilon:.2f}", flush=True)

        # Early stopping check every CHECK_INTERVAL episodes
        if ep % CHECK_INTERVAL == 0:
            avg_score = np.mean(scores[-CHECK_INTERVAL:])
            print(f"Avg over last {CHECK_INTERVAL} eps: {avg_score:.2f}")
            if avg_score > best_avg + improvement_threshold:
                best_avg = avg_score
                patience_counter = 0
            else:
                patience_counter += 1
                if patience_counter >= EARLY_STOP_PATIENCE:
                    print("\nEarly stopping: no improvement detected.\n")
                    break

    print("\nTraining finished!\n")
    print("\n" * BLANK_LINES_BEFORE_DEMO)
    print("=== Demo with rendering ===\n")
    snake_game.run_episode(bot, render=True)

# --------------------------- Helpers --------------------------- #
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def run_and_collect(bot):
    states_actions = []

    class CollectorBot:
        def next_move(_, state):
            action = bot.next_move(state)
            states_actions.append((state, action))
            return action

    res = snake_game.run_episode(CollectorBot(), render=False)

    # Build trajectory with proximity-based shaping
    trajectory = []
    for i, (state, action) in enumerate(states_actions):
        current_head = state["snake"][0]
        food = state["food"]
        distance_now = manhattan_distance(current_head, food)

        # Look at next state if available
        if i + 1 < len(states_actions):
            next_head = states_actions[i + 1][0]["snake"][0]
            distance_next = manhattan_distance(next_head, food)
        else:
            distance_next = distance_now

        # Reward shaping
        move_reward = 0
        if distance_next < distance_now:
            move_reward += 2.0  # closer to food
        else:
            move_reward -= 0.2  # moving away from food

        # Add game composite score weight (final outcome)
        move_reward += res["composite"] * 0.1

        trajectory.append((encode_state(state), action, move_reward))

    MEMORY.extend(trajectory)
    return res, trajectory

def train_on_trajectory(model, trajectory):
    if not trajectory:
        return

    X, y = [], []
    for state, action, reward in trajectory:
        idx = SnakeBotRL.DIRECTIONS.index(action)
        target = np.zeros(4)
        target[idx] = reward
        X.append(state)
        y.append(target)

    model.fit(np.array(X), np.array(y), epochs=1, verbose=0)

# --------------------------- Run --------------------------- #
if __name__ == "__main__":
    train_and_demo()
