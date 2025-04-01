import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

password_length = int(input("Enter password length: "))
print("Generated Password:", generate_password(password_length))
