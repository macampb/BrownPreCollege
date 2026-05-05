import hashlib
import requests

def check_breach(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1pwd[:5], sha1pwd[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    hashes = (line.split(':') for line in response.text.splitlines())
    return any(h == suffix for h, _ in hashes)

if __name__ == "__main__":
    test_passwords = ["123456", "Blu3P@nda2025"]
    for pwd in test_passwords:
        print(f"{pwd} breached? {check_breach(pwd)}")
