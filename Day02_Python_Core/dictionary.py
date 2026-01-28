
"""
Day 2 – Dictionary in Python
Author: Uday Kumar
"""

# dictionary

'''Student = {"name": "Rahul","age": 21,"city":"Delhi","Course":"Python"}
print("\n",Student,"\n")
print(Student["name"],"\n")
print(Student.get("age"),"\n")

print(Student.keys(),"\n")
print(Student.values(),"\n")

print(Student.items(),"\n")

Student["roll_no"]= 34
print(Student,"\n")

Student.update({"age": 46,"Course":"Dijango"})

print(Student)

Student.pop("city")

print(Student)

#Student.pop.items()


dict1 = {"a":2, "b":3}

dict2 = dict1.copy()

print(dict2)


dict2 = {"c":4,"d":5}

dict1.update(dict2)
print(dict1)

# Clear Dictionary

Student.clear()

print(Student)'''


# Practice of Dictionary

# Dictionary storing mobile details

'''
mobile = {"brand": "samsong", "model": "s24", "price": "75K", "stock": "1K"}

# Print the entire dictionary
print("\n", mobile, "\n")

# Print all keys of the dictionary
print(mobile.keys(), "\n")

# Print all key-value pairs as tuples
print(mobile.items(), "\n")

# Print total number of key-value pairs
print(len(mobile), "\n")

# Access and print value of 'brand' key
print(mobile["brand"])

# Print all values in the dictionary
print(mobile.values(), "\n")

# Change value of the 'brand' key
mobile["brand"] = "VIVO"

# Print updated dictionary
print(mobile, "\n")

# Update multiple key-value pairs at once
mobile.update({"brand": "samsong", "stock": "5K"})

# Print dictionary after update
print(mobile, "\n")

# Remove the 'stock' key and its value
mobile.pop("stock")

# Print dictionary after removing 'stock'
print(mobile, "\n")

# Remove the last inserted key-value pair
mobile.popitem()

# Print final dictionary
print(mobile)'''
