import requests

BASE_URL = "http://127.0.0.1:5000"

# ✅ 1. Test Password Strength + Breach
print("Testing /check_strength endpoint...")
password = {"password": "Blu3P@nda2025"}
response = requests.post(f"{BASE_URL}/check_strength", json=password)
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code)

print("\n" + "="*50 + "\n")

# ✅ 2. Test Personalized Password Generator
print("Testing /generate_password endpoint...")
answers = {
    "color": "blue",
    "animal": "panda",
    "hobby": "gaming",
    "year": "2031",
    "symbol": "@",
    "lucky_number": 7
}
response = requests.post(f"{BASE_URL}/generate_password", json=answers)
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code)
