# Create file and write name & city
'''file = open("data.txt", "w")
file.write("Name: Uday\n")
file.write("City: Delhi\n")
file.close()'''

'''file = open("data.txt", "r")
content = file.read()
print(content)
file.close()'''


# Append age
'''
file = open("data.txt", "a")
file.write("Age: 22\n")
file.close()'''

# Read file content
'''file = open("data.txt", "r")
content = file.read()
print(content)
file.close()'''

# ---------- READ FIRST LINE ----------
file = open("data.txt", "r")
line = file.readline()
print("Using readline():")
print(line)
file.close()

# ---------- READ ALL LINES AS LIST ----------
file = open("data.txt", "r")
lines = file.readlines()
print("Using readlines():")
print(lines)
file.close()

print(len(lines))
