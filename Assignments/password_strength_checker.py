# Home work
'''1.generate random password
2.check password strength
3.count character used in password
4.gives a strength score using math
5.saves the result in a file using os'''

import random
import string
import math
import os
import re
from collections import Counter

# 1. Generate Random Password

all_chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(all_chars) for _ in range(12))

# 2. Check Password Strength (Using Regex)

has_upper = bool(re.search(r"[A-Z]", password))
has_lower = bool(re.search(r"[a-z]", password))
has_digit = bool(re.search(r"[0-9]", password))
has_special = bool(re.search(r"[^\w]", password))

strength = "Weak"

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    strength = "Strong"
elif len(password) >= 6:
    strength = "Medium"


# 3. Count Characters (Using Counter)

char_counter = Counter(password)

upper = sum(1 for c in password if c.isupper())
lower = sum(1 for c in password if c.islower())
digits = sum(1 for c in password if c.isdigit())
special = sum(1 for c in password if c in string.punctuation)


# 4. Strength Score Using Math

unique_chars = len(set(password))
length = len(password)

score = math.sqrt(unique_chars * length) * 10
score = round(score, 2)


# 5. Save Using OS

if not os.path.exists("easy_reports"):
    os.mkdir("easy_reports")

file_path = os.path.join("easy_reports", "password_report.txt")

with open(file_path, "w") as file:
    file.write(f"Password: {password}\n")
    file.write(f"Strength: {strength}\n")
    file.write(f"Score: {score}\n\n")

    file.write("Character Types:\n")
    file.write(f"Uppercase: {upper}\n")
    file.write(f"Lowercase: {lower}\n")
    file.write(f"Digits: {digits}\n")
    file.write(f"Special: {special}\n\n")

    file.write("Character Frequency (Counter):\n")
    for ch, count in char_counter.items():
        file.write(f"{ch} : {count}\n")

# Output
print("Password:", password)
print("Strength:", strength)
print("Score:", score)
print("Upper:", upper)
print("Lower:", lower)
print("Digits:", digits)
print("Special:", special)
print("Counter:", char_counter)
print("Saved At:", file_path)
