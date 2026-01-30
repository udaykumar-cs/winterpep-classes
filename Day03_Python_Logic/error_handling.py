

# 1. ZeroDivisionError
try:
    a = 10
    b = 0
    result = a / b  # Cannot divide by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
finally:
    print("Division attempt completed\n")


# 2. IndexError
nums = [1, 2, 3]
try:
    print(nums[5])  # Index out of range
except IndexError:
    print("Error: Index out of range")
finally:
    print("Index check completed\n")


# 3. ValueError
try:
    num = int("abc")  # Cannot convert string to int
except ValueError:
    print("Error: Invalid integer conversion")
finally:
    print("Value conversion attempt completed\n")


# 4. KeyError
my_dict = {"name": "Uday", "age": 25}
try:
    print(my_dict["salary"])  # Key does not exist
except KeyError:
    print("Error: Key not found in dictionary")
finally:
    print("Dictionary key check completed\n")


# 5. TypeError
try:
    result = "10" + 5  # Cannot add string and integer
except TypeError:
    print("Error: Invalid operation between incompatible types")
finally:
    print("Type check completed\n")


# 6. FileNotFoundError
try:
    file = open("nonexistent_file.txt", "r")  # File does not exist
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("File operation attempted\n")


# 7. AttributeError
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Uday")
try:
    print(p.age)  # Attribute does not exist
except AttributeError:
    print("Error: Attribute not found in object")
finally:
    print("Attribute access attempted\n")


# 8. ImportError
''' try:
    import non_existing_module  # Module does not exist
except ImportError:
    print("Error: Module not found")
finally:
    print("Module import attempted\n") '''


# 9. General Exception
try:
    x = 10 / 2  # This is safe
    print("Division result:", x)
except Exception as e:  # Catch any unexpected error
    print("Unexpected error:", e)
else:  # Runs only if no exception occurs
    print("No exception occurred")
finally:
    print("General exception handling completed\n")


# 10. Multiple Exceptions
try:
    x = int("abc") / 0  # Could raise ValueError or ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:  # Handle both exceptions
    print("Error occurred:", e)
finally:
    print("Multiple exception check completed\n")
