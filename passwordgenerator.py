import random
import os

# Base of symbols to choose from
SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*", "?", ";"]

# Function to randomize letter case
def randomize_case(text):
    return "".join(c.upper() if random.choice([True, False]) else c.lower() for c in text)

# Function to generate password
def generate_password(name, city, max_len=20):
    number = random.randint(100, 999)
    symbol1 = random.choice(SYMBOLS)
    symbol2 = random.choice(SYMBOLS)
    symbol3 = random.choice(SYMBOLS)
    name_random = randomize_case(name)
    city_random = randomize_case(city)
    password = name_random + symbol1 + city_random + symbol2 + str(number) + symbol3
    return password[:max_len]

# Function to check if password is strong
def is_strong(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in SYMBOLS for c in password)
    long_enough = len(password) >= 15
    return all([has_upper, has_lower, has_digit, has_symbol, long_enough])

# Function to save password to file (append mode)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASSWORD_FILE = os.path.join(BASE_DIR, "password.txt")
if not os.path.exists(PASSWORD_FILE):
    open(PASSWORD_FILE, "w").close()
def save_password(password):
    with open(PASSWORD_FILE, "a", encoding="utf-8") as file:
        file.write(password + "\n")

# Main Program
print("THIS IS A SCRIPT FOR PHILOSOPHER'S ENTHUSIASTS TO GENERATE STRONG PASSWORDS")

name = input("Enter philosopher's name: ").strip()
city = input("Enter philosopher's city: ").strip()

password = generate_password(name, city)

if is_strong(password):
    save_password(password)
    print(f"Password: {password} is strong and has been saved.")
else:
    print(f"Password: {password} is not strong enough. Not saved.")


