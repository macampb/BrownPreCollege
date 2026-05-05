# app/generator.py
import random
import string

def personalized_password(answers):
    """
    Randomized Structure Mode:
    - Fully randomizes order of user inputs
    - Applies 1–2 smart substitutions
    - Capitalizes first letters for readability
    - Ensures length 7–16, includes at least 1 special char and 1 digit
    """

    # Collect user inputs
    components = [
        answers.get('color', '').strip().capitalize(),
        answers.get('animal', '').strip().capitalize(),
        answers.get('hobby', '').strip().capitalize(),
        str(answers.get('year', '')).strip(),
        answers.get('symbol', '').strip(),
        str(answers.get('lucky_number', '')).strip()
    ]

    # Remove empty values
    components = [c for c in components if c]

    # Randomize order completely
    random.shuffle(components)

    # Combine into a single password string
    password = ''.join(components)

    # Apply 1–2 smart substitutions for extra strength
    subs_map = {'a': '@', 's': '$', 'i': '1', 'o': '0'}
    password_chars = list(password)
    candidates = [i for i, ch in enumerate(password_chars) if ch.lower() in subs_map]

    if candidates:
        num_subs = min(random.randint(1, 2), len(candidates))
        for i in random.sample(candidates, num_subs):
            password_chars[i] = subs_map[password_chars[i].lower()]

    password = ''.join(password_chars)

    # Ensure at least one special character
    if not any(c in string.punctuation for c in password):
        password += random.choice("!@#$%^&*")

    # Ensure at least one digit
    if not any(c.isdigit() for c in password):
        password += str(random.randint(0, 9))

    # Enforce length between 7 and 16 characters
    if len(password) < 7:
        while len(password) < 7:
            password += random.choice(string.ascii_letters + string.digits)
    elif len(password) > 16:
        password = password[:16]

    return password
