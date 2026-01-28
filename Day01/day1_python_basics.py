
"""
Day 1 – Python Basics (PEP Classes)

Topics Covered:
- Print statements
- Variables & Data Types
- Type Conversion
- Conditional Statements
- Loops (for, while)
- Functions & Lambda
- List, Set, Tuple
- Memory reference (id)

Author: Uday Kumar
"""


'''print ("Hello World")
name = "Uday Kumar"
print(name)
height = 5.11
print(height)
print(type(height))
x = "100"
print(x)
print(int(x))


# Conditional'''

'''
x = int(input("Enter your input"))
if(x > 7):
    print("You are eligible to Play the Match")
else:
    print("You have to work hard")


x1 = int(input("Enter the number "))

if(x1 %2 == 0):
    print("Number entered by you is even: ", x1)
else:
    print("Number is not even you have to enter the even number")

marks = int(input("Enter the marks obtained by the Student: "))

if(marks >= 90):
    print("Grade A")
elif(marks >= 75):
    print("Grade is B ")
elif(marks >= 50 ):
    print("Grade is C ")
else:
    print("Student have to appear for the exam again")

a = int(input("Enter  thew 1st number "))
b = int(input("Enter the 2nd number "))

if(a> b):
    print("Greater number is A i.e: ", a)

else:
    print("Greater number is B i.e: ",b)


s1 = str(input("Enter the 1st String "))

if(s1 =="Red"):
    print("You Hvae to stop: ",s1)
elif(s1 =="Green"):
    print("You can Go:  ",s1)
    
elif(s2 == "Yellow"):
    print("Be ready to Go: ",s1)
else:
    print("Plz enter the valid input: ")

for i in range(1,16):
    if(i % 2 != 0):
        print(i)

x = int(input("Number "))

for i in range(x):
    print("*"*i)


num = int(input("number"))
i = 1
while(i <= 10):
    print(num,"x", i ,"=" , num*i)
    i = i+1'''



# Functions 



'''def Greet():
    print("Hey! Whats Going there")
Greet()
Greet()
Greet()


# Argument but no return type
def Add(a,b):
    print(a+b)

Add(3,4)
Add(2,5)
Add(1,6)

#Both Argument and return type

def sum(a,b):
    return(a+b)
addition = sum(7,0)
print("Sum of Given two Number is : ",addition)

add = lambda x,y : x+y
print(add(10,20))

# Square of any number using Lambda function

square = lambda x : x*x
print(square(7))
'''


# Practice

'''
# Take input print its type and then print double of it 

x = input("Enter the input: ")

print(type(x))

print(x*2)

# Take input salary as string then convert it to integer and add bonous 500 and print

salary =(input("Enter the salary "))

s = int(salary)
print("New salary is: ",s+ 500)

# Print Hot If temp > 30 , normal temp>= 15 , else cold

temp = float(input("Enter the temp: "))

if(temp >= 30):
    print("Weather is Hot ")
elif(temp >= 15):
    print("Wether is Noraml")
else:
    print("Whether is Cold ")

# Create a lambda Function to return a cube
n = int(input("Enter the number that you want to cube: "))
cube = lambda x : x*x*x
print("Cube of the given number is: ",cube(n))

# Check even odd using Function 
num = int(input("Enter the number that you want to check Odd or Even "))
def checknum(a):
    if(a %2 == 0):
        print("Number is Even: ")
    else:
        print("Number is odd ")
checknum(num)



# Take a number and reverse it using while loop

number = int(input("Enter the number to reverse: "))
rev = 0

while number > 0:
    digit = number % 10        
    rev = rev * 10 + digit     
    number = number // 10      

print("Reversed number:", rev)

# Print table of 7 and also count how many numbers are printed
count = 0
num = int(input("Enter the Number to make table of that "))
for i in range(1,11):
    print(num,"*",i,"=", num*i)
    count = count + 1
print("Total Number printed are: ",count)'''

# Python datastructure 



# List 

'''marks = [10, 20, 30, 40] # List of integers

print(marks[1])

#Append
marks.append(100)
print(marks)
print(marks[-1])

# Insert
marks.insert(2,75)
print(marks)


# Marks.remove
marks.remove(75)

print(marks)

print(marks.pop())



# sort 

age = [23,25,19,18,36]
age.sort()
print(age)
age.reverse()
print(age)

# Len of list age 
print(len(age))

print(max(age))

print(sum(age))

print(sum(age)/len(age))'''

# Practice List
'''
# Create a list of 5 cities
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru"]
print("Original list:", cities)

#Length
print(len(cities))

# append(): 
cities.append("Hyderabad")
print("After append():", cities)

# extend(): 
cities.extend(["Pune", "Jaipur"])
print("After extend():", cities)

# insert(): 
cities.insert(2, "Ahmedabad")
print("After insert():", cities)

# sort()- sort the list
cities.sort()
print("After sort():", cities)

# reverse()- reverse the list
cities.reverse()
print("After reverse():", cities)


# clear(): 
cities.clear()
print("After clear():", cities)'''


# Set Implementation


'''numbers = {10,20,30,40,10}
print(numbers)

for i in numbers:
    print(i)

numbers.add(100)
print(numbers)

numbers.update([120,130])

print(numbers)

# print(numbers.remove(155)) // Give error when not present in the number is not present in the set


numbers.discard(175)
print(numbers)

numbers.pop()

print(numbers)''' 

# Set Practice

'''
# Create a set of marks

marks = {85, 90, 78, 92, 85}
print("Original set of marks:", marks)

# Traversing the set

print("\nMarks in the set:")
for m in marks:
    print(m)

# add() – add a single element
marks.add(88)
print("\nAfter add():", marks)

# update() – add multiple elements
marks.update([95, 80, 70])
print("After update():", marks)

# remove() – removes element (error if not present)
# marks.remove(100)  # Uncomment to see error

# discard() – removes element (no error if not present)

marks.discard(100)
print("After discard():", marks)

# pop() – removes a random element
marks.pop()
print("After pop():", marks)

# len() – number of elements
print("Length of set:", len(marks))

# max() – maximum value
print("Maximum marks:", max(marks))

# min() – minimum value
print("Minimum marks:", min(marks))

# sum() – sum of all elements
print("Total marks:", sum(marks))

# copy() – copy the set
marks_copy = marks.copy()
print("Copied set:", marks_copy)

# clear() – remove all elements
marks.clear()
print("After clear():", marks)'''



# Tuple Implementation

'''days=("monday","tuesday","wednesday","Thrusday","Friday","Sataurday","Sunday")

print(days)
print(days[3])
print(days.count("monday"))
print(len(days))

print(days[1:4])

print("monday" in days)'''


# Tuple Practice


# Create a tuple of 6 friends


friends = ("Aman", "Rohit", "Neha", "Priya", "Karan", "Sneha")

print("Friends tuple:", friends)

# len() – length of tuple
print("Length of tuple:", len(friends))

# count() – count occurrences of an element
print("Count of 'Neha':", friends.count("Neha"))

# index() – find index of an element
print("Index of 'Priya':", friends.index("Priya"))

# slicing – get a subset of tuple 
print("Slicing (index 1 to 4):", friends[1:5])

# in – membership operator
print("Is 'Karan' in tuple?", "Karan" in friends)
print("Is 'Rahul' in tuple?", "Rahul" in friends)

# 
x = 5
y = x
x = 6
print(x)
print(y)
print(id(x))
print(id(y))



