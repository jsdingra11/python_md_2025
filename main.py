# =======================================================================
#
#   PYTHON PRACTICAL FILE (B.TECH CBEGS 2024-2025)
#
#   This file contains all the Python code for the practicals
#   in the final report. Each section is marked with a header.
#
# =======================================================================

print("\n" + "="*50 + "\n")
print("   Practical 1: Variables, Constants, and Data Types")
print("="*50 + "\n")

# --- Variables and Assignment ---
# A variable is like a labeled box. Here, the box is 'website'
# and the data we put in it is "github.com".
website = "github.com"
print(website)

# We can change the data in the box (re-assignment)
website = "baidu.com"
print(website)

# Multiple assignment in one line
a, b, c = 6, 9.3, "Hello"
print(a)
print(b)
print(c)

# --- Constants (By Convention) ---
# Constants are variables that shouldn't change.
# We write them in ALL_CAPS to show this.
PI = 3.14
GRAVITY = 9.8
print(PI)

# --- Data Types (The 'type' of data) ---
print("\n--- Data Types ---")

# 1. Numbers (int, float, complex)
a_int = 6           # int (whole number)
a_float = 3.0       # float (decimal number)
a_complex = 1+2j    # complex (math number)
print(a_int, "is of type", type(a_int))
print(a_float, "is of type", type(a_float))
print(a_complex, "is of type", type(a_complex))

# 2. String (str) - for text
s = "Hello world!"
print(s, "is of type", type(s))

# 3. List (list) - ordered, changeable
x = [6, 99, 77, 'Apple']
print(x, "is of type", type(x))
x[1] = 100 # Lists are mutable (changeable)
print("Modified list:", x)

# 4. Tuple (tuple) - ordered, NOT changeable
t = (6, 'program', 1+3j)
print(t, "is of type", type(t))
# t[0] = 10 # This would cause an error!

# 5. Set (set) - unordered, unique items
a_set = {1, 2, 2, 3, 3, 3} # Duplicates are automatically removed
print(a_set, "is of type", type(a_set))

# 6. Dictionary (dict) - key-value pairs
d = {1: 'Apple', 2: 'Cat', 3: 'Food'}
print(d, "is of type", type(d))
print("Value for key 1 is:", d[1])


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 2: Python Operators")
print("="*50 + "\n")
# =======================================================================

# --- 1. Arithmetic Operators (Math) ---
x = 16
y = 3
print('x + y =', x + y)       # Addition
print('x - y =', x - y)       # Subtraction
print('x * y =', x * y)       # Multiplication
print('x / y =', x / y)       # Division (always gives a float)
print('x // y =', x // y)   # Floor Division (drops the decimal)
print('x % y =', x % y)       # Modulus (the remainder)
print('x ** y =', x ** y)     # Exponentiation (x to the power of y)

# --- 2. Comparison Operators (True/False) ---
print("\n--- Comparison ---")
print('6 > 3 is', 6 > 3)       # Greater than
print('6 < 3 is', 6 < 3)       # Less than
print('6 == 3 is', 6 == 3)     # Equal to
print('6 != 3 is', 6 != 3)     # Not equal to
print('6 >= 3 is', 6 >= 3)     # Greater than or equal to

# --- 3. Logical Operators (and, or, not) ---
print("\n--- Logic ---")
print('True and False is', True and False) # 'and' checks if BOTH are true
print('True or False is', True or False)   # 'or' checks if AT LEAST ONE is true
print('not True is', not True)             # 'not' flips the value

# Combining operators
print('6 > 3 and 5 < 3 is', 6 > 3 and 5 < 3) # (True and False) -> False
print('6 > 3 or 5 < 3 is', 6 > 3 or 5 < 3)   # (True or False)  -> True


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 3: Input, Output, and String Formatting")
print("="*50 + "\n")
# =======================================================================

# --- 1. Output with print() ---
a = 9
print('The value of a is', a) # print() automatically adds a space

# Using 'sep' (separator)
print(1, 2, 3, 4, sep='#') # Use '#' instead of a space

# Using 'end'
print(1, 2, 3, 4, sep='*', end='&')
print("...next print starts right here.")

# --- 2. String Formatting (str.format) ---
print("\n--- Formatting ---")
x = 6
y = 12
# The {} are placeholders
print('The value of x is {} and y is {}'.format(x, y))

# You can use numbers to change the order
print('I love {0} and {1}'.format('Mango', 'Banana'))
print('I love {1} and {0}'.format('Mango', 'Banana'))

# You can use names
print('Hello {name}, {greeting}!'.format(greeting='Good morning', name='Mark'))

# --- 3. Input with input() ---
print("\n--- Input ---")
# We 'try...except' to avoid crashing if the user just hits Enter
try:
    num_str = input('Enter a number: ')
    print("You entered:", num_str)
    print("Type of input is:", type(num_str)) # Input is ALWAYS a string!
except EOFError:
    print("No input provided.")


# --- 4. Type Casting Input ---
# To do math, we must convert the string to a number (int or float)
print("\n--- Type Casting ---")
try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    sum1 = first_number + second_number
    print("Addition of two numbers is:", sum1)
except (ValueError, EOFError):
    print("Invalid input. Please enter whole numbers.")


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 4: Decision Structures (if-elif-else)")
print("="*50 + "\n")
# =======================================================================

# --- 1. Simple if statement ---
# This block only runs if the condition is True.
age = 20
if age >= 18:
    print("You are eligible to vote.")

# --- 2. if-else statement ---
# One of these two blocks will ALWAYS run.
try:
    num = int(input("Enter a number to check even/odd: "))
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")
except (ValueError, EOFError):
    print("Invalid input. Please enter a whole number.")


# --- 3. if-elif-else statement ---
# 'elif' means "else if". It checks conditions in order.
# Only ONE block will run (the first one that is True).
try:
    score = int(input("Enter your test score: "))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F' # The 'else' catches everything else.
    print("Your grade is:", grade)
except (ValueError, EOFError):
    print("Invalid input. Please enter a whole number.")


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 5: Repetition Structures (Loops)")
print("="*50 + "\n")
# =======================================================================

# --- 1. while Loop ---
# This loop will run as long as 'i' is less than or equal to 5.
print("--- while Loop ---")
total = 0
i = 1
while i <= 5:
    total = total + i
    i = i + 1   # We must increment 'i' ourselves!
print("The sum of numbers from 1 to 5 is", total)

# --- 2. for Loop (with range) ---
# This is a "count-controlled" loop.
# range(5) gives numbers 0, 1, 2, 3, 4.
print("\n--- for Loop with range(5) ---")
for i in range(5):
    print(i, end=' ')
print() # for new line

# range(1, 6) gives numbers 1, 2, 3, 4, 5.
print("\n--- for Loop with range(1, 6) ---")
for i in range(1, 6):
    print(i, end=' ')
print()

# --- 3. for Loop (with a list) ---
# This loop runs once for each item in the 'fruits' list.
print("\n--- for Loop with a list ---")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# --- 4. Nested Loops ---
# A loop inside another loop.
print("\n--- Nested Loops (Pattern) ---")
for i in range(1, 4):     # Outer loop (rows)
    for j in range(i):  # Inner loop (columns)
        print("*", end=" ")
    print() # New line after each row


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 6: User-Defined Functions")
print("="*50 + "\n")
# =======================================================================

# --- 1. Defining and Calling a Simple Function ---
# This function takes no input and returns no value. It just does an action.
def greet():
    print("Welcome to Python for Data Science")

print("Calling greet():")
greet() # This is how we call (run) the function

# --- 2. Function with Parameters ---
# 'name' is a parameter. It's a placeholder for the data
# we will send in.
def greet_person(name):
    print("Hello, " + name + ". Good morning!")

print("\nCalling greet_person('Arthur'):")
greet_person('Arthur') # 'Arthur' is the argument (the actual data)
greet_person('Emily')

# --- 3. Value-Returning Function ---
# This function gives a value back using the 'return' keyword.
def add_two_numbers(num_one, num_two):
    total = num_one + num_two
    return total

print("\nCalling add_two_numbers(3, 6):")
sum_result = add_two_numbers(3, 6)
print("The result is:", sum_result)

# --- 4. Function with multiple parameters and return value ---
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print("\nCalling generate_full_name('Milaan', 'Parmar'):")
full_name = generate_full_name('Milaan', 'Parmar')
print('Full Name:', full_name)


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 7: Lists and Tuples Manipulation")
print("="*50 + "\n")
# =======================================================================

# --- 1. List Slicing ---
# Slicing is like cutting out a piece of the list.
# format is list[start:stop] (stop is not included)
a = [5, 10, 15, 20, 25, 30, 35, 40]
print("Original list:", a)

print("a[2] = ", a[2])           # Get one item (index 2)
print("a[0:3] = ", a[0:3])     # Get items from index 0 up to (but not in) 3
print("a[5:] = ", a[5:])       # Get items from index 5 to the end

# --- 2. List Methods (built-in functions) ---
my_list = [1, 5, 3, 5, 9]
print("\nOriginal my_list:", my_list)

my_list.append(10) # .append() adds an item to the end
print("After append(10):", my_list)

my_list.sort() # .sort() sorts the list in place
print("After sort():", my_list)

item_count = my_list.count(5) # .count() checks how many '5's are in the list
print("Count of 5:", item_count)

my_list.remove(3) # .remove() removes the first '3' it finds
print("After remove(3):", my_list)

# --- 3. Two-Dimensional Lists (List of lists) ---
print("\n--- 2D List (Matrix) ---")
matrix = [
    [1, 2, 3], # row 0
    [4, 5, 6], # row 1
    [7, 8, 9]  # row 2
]
print(matrix)
# Access element at row 1, column 1
print("Element at matrix[1][1] is:", matrix[1][1])


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 8: File Handling and Exceptions")
print("="*50 + "\n")
# =======================================================================

# --- 1. Writing to a File ("w" mode) ---
# 'with open' is the safe way to handle files.
# "w" mode means 'write' (it will create or overwrite the file)
file_content = "Hello, this is a test file.\nThis is the second line."
try:
    with open("practical_file.txt", "w") as f:
        f.write(file_content)
    print("File 'practical_file.txt' written successfully.")
except Exception as e:
    print(f"An error occurred while writing: {e}")

# --- 2. Reading from a File ("r" mode) ---
# "r" mode means 'read'
print("\n--- Reading from file ---")
try:
    with open("practical_file.txt", "r") as f:
        content = f.read() # .read() gets the whole content
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file 'practical_file.txt' was not found.")

# --- 3. Exception Handling (Catching an error) ---
print("\n--- Testing Exception Handling ---")
try:
    # We try to open a file that doesn't exist
    with open("non_existent_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    # The 'except' block catches the error
    print("Successfully caught expected error: File was not found.")

# --- 4. Processing File line by line (Loop) ---
print("\n--- Reading file line-by-line ---")
try:
    with open("practical_file.txt", "r") as f:
        for line in f:
            print("Line:", line.strip()) # .strip() removes whitespace/newlines
except FileNotFoundError:
    print("Error: The file 'practical_file.txt' was not found.")


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 9: Advanced String Manipulation")
print("="*50 + "\n")
# =======================================================================

# --- 1. String Slicing ---
# Works just like list slicing!
s = 'Hello world!'
print("Original string:", s)

print("s[4] = ", s[4])         # Get one character
print("s[6:11] = ", s[6:11])   # Get a sub-string

# --- 2. String Methods ---
# Note: Strings are IMMUTABLE.
# Methods don't change the original string, they return a NEW string.
text = "  Python is Fun!  "
print("\nOriginal text: '" + text + "'")

# Manipulating
print("strip(): '" + text.strip() + "'")     # Removes whitespace from ends
print("upper(): " + text.upper())       # Converts to uppercase
print("lower(): " + text.lower())       # Converts to lowercase
print("replace('Fun', 'Great'): " + text.replace("Fun", "Great"))

# Searching / Testing
print("startswith('  Python'):", text.startswith('  Python'))
print("find('is'):", text.find('is')) # Returns the index where 'is' starts

# Splitting
# .split() turns a string into a list of strings
words = text.strip().split(' ')
print("split(' '):", words)


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 10: Dictionaries and Sets")
print("="*50 + "\n")
# =======================================================================

# --- 1. Sets ---
# Note how the duplicates (2, 3, 5) are removed
a = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print("Set 'a':", a)
print("Type of 'a':", type(a))

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("\nSet1:", set1)
print("Set2:", set2)
print("Union (set1 | set2):", set1 | set2)           # All items from both
print("Intersection (set1 & set2):", set1 & set2)   # Only items in both
print("Difference (set1 - set2):", set1 - set2)   # Items in set1, but not set2


# --- 2. Dictionaries ---
# {key: value, key: value}
d = {1: 'value', 'key': 2}
print("\nDictionary 'd':", d)
print("Type of 'd':", type(d))

# Accessing values by key
print("d[1] = ", d[1])
print("d['key'] = ", d['key'])

# Adding a new key-value pair
d[3] = 'New Item'
print("After adding d[3]:", d)

# Iterating over a dictionary
print("\nIterating over dictionary:")
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")


# =======================================================================
print("\n" + "="*50 + "\n")
print("   Practical 11: Classes and Object-Oriented Programming")
print("="*50 + "\n")
# =======================================================================

# --- Defining a Class ---
# This is the "blueprint" for a Student.
class Student:
    # Class attribute (shared by all students)
    species = "students"
    student_count = 0 

    # The Constructor (__init__) runs when a NEW object is created
    # 'self' refers to the object being created (e.g., s1 or s2)
    def __init__(self, name, id):
        # Instance attributes (data unique to this object)
        self.name = name
        self.id = id
        self.skills = [] # A new empty list for each new student
        Student.student_count += 1 # Update the shared count

    # Instance method (a function that objects can do)
    def printStudentData(self):
        print("Name:", self.name, ", Id:", self.id)

    # Another instance method
    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"Added skill '{skill}' for {self.name}")

# --- Creating and Using Instances (Objects) ---
print("Total Students:", Student.student_count)

# Create first instance
print("\n--- Creating s1 ---")
s1 = Student("Arthur", 101) # This calls __init__
s1.printStudentData()       # This calls the object's method
s1.add_skill("HTML")

# Create second instance
print("\n--- Creating s2 ---")
s2 = Student("Emily", 102)
s2.printStudentData()
s2.add_skill("Marketing")

# --- Final Status ---
print("\n--- Final Status ---")
print("s1 skills:", s1.skills) # Note: s1 and s2 have different skill lists
print("s2 skills:", s2.skills)
print("Total Students:", Student.student_count) # The shared count is 2

# =======================================================================
print("\n" + "="*50 + "\n")
print("   End of Practical File")
print("="*50 + "\n")
# =======================================================================
