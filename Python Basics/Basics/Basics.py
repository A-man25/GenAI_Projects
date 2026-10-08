# ============================================================
# BASIC PYTHON - NOTES & PRACTICE
# ============================================================


# ------------------------------------------------------------
# 1. FIRST PYTHON PROGRAM
# ------------------------------------------------------------

print("Welcome to Python")

# Note:
# In Python, indentation has meaning.
# It is used to define blocks of code.


# ------------------------------------------------------------
# 2. VARIABLES AND BASIC DATA TYPES
# ------------------------------------------------------------

# Python supports several built-in data types:
#
# int   -> Whole numbers
#          Example: 10, -5
#
# float -> Decimal numbers
#          Example: 3.14, -0.001
#
# str   -> Text enclosed in quotes
#          Example: "Hello", 'Python'
#
# bool  -> True or False
#
# list  -> Ordered, mutable collection
#          Example: [1, 2, 3]
#
# tuple -> Ordered, immutable collection
#          Example: (1, 2, 3)
#
# set   -> Unordered collection of unique elements
#          Example: {1, 2, 3}
#
# dict  -> Key-value pairs
#          Example: {"name": "Alice", "age": 25}


# Integer
num = 1

print(num)
print(type(num))


# String
string_value = "This is a string"

print(string_value)
print(type(string_value))


# Python does NOT have a separate char data type.
# A single character is simply a string of length 1.

char_value = "a"

print(char_value)
print(type(char_value))


# Boolean
# Boolean values must use capital T and F:
# True
# False

bool_value = True

print(bool_value)
print(type(bool_value))


# Float
float_value = 4.5

print(float_value)
print(type(float_value))


# ------------------------------------------------------------
# 3. TYPE CASTING
# ------------------------------------------------------------

# Common type casting functions:
#
# int()
# float()
# str()
# bool()


x = "20"
y = 5

x = int(x)

print(x + y)
print(type(x + y))


# Converting float to int

x = 8.9

print(int(x))

# Output:
# 8
#
# int() does NOT round the number.
# It simply removes/truncates the decimal part.


# Converting string to bool

x = "False"
y = bool(x)

print(y)

# Output:
# True
#
# Why?
# bool() checks whether the string is empty.
#
# Empty string:
# bool("") -> False
#
# Non-empty string:
# bool("False") -> True
# bool("Hello") -> True


# ------------------------------------------------------------
# 4. USER INPUT
# ------------------------------------------------------------

# input() is used to take input from the user.
#
# Important:
# input() always returns a string.

x = input("Enter a number: ")

print(x)
print(type(x))


# If we want the input as an integer:

number = int(input("Enter another number: "))

print(number)
print(type(number))


# ------------------------------------------------------------
# 5. BASIC IF STATEMENT
# ------------------------------------------------------------

a = 5
b = 67

if a < b:
    print(a)

# Parentheses are not required:
#
# if (a < b):
#
# works, but Python usually prefers:
#
# if a < b:


# ------------------------------------------------------------
# 6. PRINT SEPARATOR - sep
# ------------------------------------------------------------

# By default, print() separates multiple values using a space.

print("Hello", "Aman")

# Output:
# Hello Aman


# We can change the separator using sep.

print("Hello", "Aman", sep=":")

# Output:
# Hello:Aman


print("Python", "C++", "AI", sep=" | ")

# Output:
# Python | C++ | AI


# ------------------------------------------------------------
# 7. PRINT END - end
# ------------------------------------------------------------

# By default, print() ends with:
#
# \n
#
# which means "new line".

print("Hello")
print("Aman")

# Output:
# Hello
# Aman


# We can change this using end.

print("Hello", end=" ")
print("Aman")

# Output:
# Hello Aman


print("A", end=" -> ")
print("B", end=" -> ")
print("C")

# Output:
# A -> B -> C 

# ------------------------------------------------------------
# 7 PYTHON REPL
# ------------------------------------------------------------

# REPL stands for:
# Read - Eval - Print - Loop
#
# It is an interactive Python environment where we can execute
# Python code one line at a time and immediately see the result.
#
# Example:
# >>> 2 + 3
# 5
#
# >>> name = "Aman"
# >>> print(name)
# Aman
#
# To enter the Python REPL from the terminal:
# python
#
# When we see:
# >>>
# it means we are currently inside the Python REPL.
#
# Difference:
# REPL            -> Used for quick testing and experiments.
# Python .py file -> Used to write and run complete programs.
#
# To run a Python file:
# python Basics.py


# ------------------------------------------------------------
# 8. OPERATORS
# ------------------------------------------------------------

a = 34
b = 2


# ------------------------------------------------------------
# ARITHMETIC OPERATORS
# ------------------------------------------------------------

# Arithmetic operators are used to perform mathematical operations.

print("a + b =", a + b, "-> Addition operator")
print("a - b =", a - b, "-> Subtraction operator")
print("a * b =", a * b, "-> Multiplication operator")
print("a / b =", a / b, "-> Division operator")
print("a % b =", a % b, "-> Modulo operator - gives the remainder")
print("a // b =", a // b, "-> Floor division operator")
print("a ** b =", a ** b, "-> Exponentiation operator")

# Example:
# 34 / 2  -> 17.0
# Normal division always returns a float.
#
# 34 // 2 -> 17
# Floor division removes the decimal/fractional part by rounding down.
#
# 34 % 2  -> 0
# Modulo gives the remainder.
#
# 34 ** 2 -> 1156
# Means 34 raised to the power 2.


# ------------------------------------------------------------
# COMPARISON OPERATORS
# ------------------------------------------------------------

# Comparison operators compare two values.
# They always return either True or False.

print("a == b :", a == b)   # Equal to
print("a != b :", a != b)   # Not equal to
print("a > b  :", a > b)    # Greater than
print("a < b  :", a < b)    # Less than
print("a >= b :", a >= b)   # Greater than or equal to
print("a <= b :", a <= b)   # Less than or equal to


# ------------------------------------------------------------
# ASSIGNMENT OPERATORS
# ------------------------------------------------------------

# Assignment operators are used to assign or update values.

x = 10

print("Initial x =", x)

x += 5      # Same as: x = x + 5
print("x += 5 :", x)

x -= 3      # Same as: x = x - 3
print("x -= 3 :", x)

x *= 2      # Same as: x = x * 2
print("x *= 2 :", x)

x /= 4      # Same as: x = x / 4
print("x /= 4 :", x)

x %= 3      # Same as: x = x % 3
print("x %= 3 :", x)

x = 10
x //= 3     # Same as: x = x // 3
print("x //= 3 :", x)

x = 2
x **= 3     # Same as: x = x ** 3
print("x **= 3 :", x)


# ------------------------------------------------------------
# LOGICAL OPERATORS
# ------------------------------------------------------------

# Logical operators are used to combine conditions.
#
# and -> True only when BOTH conditions are True.
# or  -> True when AT LEAST ONE condition is True.
# not -> Reverses the Boolean value.

age = 25
has_license = True

print(age >= 18 and has_license)
# True because both conditions are True.

print(age < 18 or has_license)
# True because at least one condition is True.

print(not has_license)
# False because has_license is True and 'not' reverses it.


# ------------------------------------------------------------
# MEMBERSHIP OPERATORS
# ------------------------------------------------------------

# Membership operators check whether a value exists
# inside a sequence such as a string, list, tuple, etc.
#
# in
# not in

name = "Aman"

print("A" in name)          # True
print("z" in name)          # False
print("z" not in name)      # True

numbers = [10, 20, 30, 40]

print(20 in numbers)        # True
print(100 not in numbers)   # True


# ------------------------------------------------------------
# IDENTITY OPERATORS
# ------------------------------------------------------------

# Identity operators check whether two variables refer to
# the SAME object in memory.
#
# is
# is not
#
# IMPORTANT:
# == checks if VALUES are equal.
# is checks if they are the SAME object.

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)      # True  -> values are equal
print(x is y)      # False -> different objects
print(x is z)      # True  -> same object

print(x is not y)  # True


# ------------------------------------------------------------
# BITWISE OPERATORS
# ------------------------------------------------------------

# Bitwise operators work on the binary representation of numbers.
#
# &  -> AND
# |  -> OR
# ^  -> XOR
# ~  -> NOT
# << -> Left Shift
# >> -> Right Shift

a = 5      # Binary: 0101
b = 3      # Binary: 0011

print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
