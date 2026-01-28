"""
Day 2 – String Operations
Author: Uday Kumar
"""

# STRING 
'''
# String declaration
s = "python programming"

# Length of string
print(len(s))

# First character
print(s[0])

# Last character
print(s[-1])

# First four characters
print(s[:4])

# Convert to lowercase
print(s.lower())

# Convert to uppercase
print(s.upper())

# Remove leading and trailing spaces
print(s.strip())

# Replace 'python' with 'java'
print(s.replace("python", "java"))

# Find index of first 'o'
print(s.find("o"))

# Split string into words
word = s.split()
print(word)

# Alphabet string
a = "abc"

# Check if only alphabets
print(a.isalpha())

# Check if digits
print(a.isdigit())

# Digit string
b = "123"

# Check if alphabets
print(b.isalpha())

# Check if digits
print(b.isdigit())

# Count occurrences of 'p'
print(s.count("p"))

# Print original string
print(s)

# Check if string starts with 'ja'
print(s.startswith("ja"))

# Check if string ends with 'ing'
print(s.endswith("ing"))

#REVERSE STRING

print(s[0:0:-1])

print(s[::-1])'''

# question 
'''
s = "Programming"

count = 0

for i in s:
    if i in 'aeiou':
        count+=1

print(count)'''

# q2 STRING IS PELINDROM OR NOT
'''
s1 = input("Enter the character: ")

if s1 == s1[::-1]:
    print("String is Pelindrom")
else:
    print("Entered String is not pelindrom")


s1 = input("Enter the string: ")

left = 0                 # pointer at start
right = len(s1) - 1      # pointer at end

is_palindrome = True

while left < right:
    if s1[left] != s1[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("String is Palindrome")
else:
    print("String is not Palindrome")'''

# Frequency count 

'''s = "apple"
for ch in s:
    print(ch,":",s.count(ch))


# Replace vowel with *

s = "python"
result=""
for ch in s:
    if ch in "aeiou":
        result+="*"
    else:
        result+=ch
print(result)'''