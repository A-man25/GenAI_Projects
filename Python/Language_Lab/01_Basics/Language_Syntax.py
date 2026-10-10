# ============================================================================
#                       BASIC PYTHON - NOTES & PRACTICE
# ============================================================================

print("\n" + "=" * 72)
print("                 BASIC PYTHON - NOTES & PRACTICE")
print("=" * 72)


# ----------------------------------------------------------------------------
# 1. FIRST PYTHON PROGRAM
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("1. FIRST PYTHON PROGRAM")
print("-" * 72)

print("Welcome to Python")

# Note:
# In Python, indentation has meaning.
# It is used to define blocks of code.


# ----------------------------------------------------------------------------
# 2. VARIABLES AND BASIC DATA TYPES
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("2. VARIABLES AND BASIC DATA TYPES")
print("-" * 72)

# Python supports several built-in data types:
# int   -> Whole numbers
#          Example: 10, -5
# float -> Decimal numbers
#          Example: 3.14, -0.001
# str   -> Text enclosed in quotes
#          Example: "Hello", 'Python'
# bool  -> True or False
# list  -> Ordered, mutable collection
#          Example: [1, 2, 3]
# tuple -> Ordered, immutable collection
#          Example: (1, 2, 3)
# set   -> Unordered collection of unique elements
#          Example: {1, 2, 3}
# dict  -> Key-value pairs
#          Example: {"name": "Alice", "age": 25}

# Integer
num = 1
print(f"Integer value  : {num}")
print(f"Type           : {type(num)}")

# String
string_value = "This is a string"
print(f"\nString value   : {string_value}")
print(f"Type           : {type(string_value)}")

# Python does NOT have a separate char data type.
# A single character is simply a string of length 1.
char_value = "a"
print(f"\nCharacter      : {char_value}")
print(f"Type           : {type(char_value)}")

# Boolean
# Boolean values must use capital T and F: True / False
bool_value = True
print(f"\nBoolean value  : {bool_value}")
print(f"Type           : {type(bool_value)}")

# Float
float_value = 4.5
print(f"\nFloat value    : {float_value}")
print(f"Type           : {type(float_value)}")


# ----------------------------------------------------------------------------
# 3. TYPE CASTING
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("3. TYPE CASTING")
print("-" * 72)

# Common type casting functions:
# int()
# float()
# str()
# bool()

x = "20"
y = 5

print(f"Before casting : x = {x}, type = {type(x)}")
x = int(x)
print(f"After casting  : x = {x}, type = {type(x)}")
print(f"x + y          : {x + y}")

# Converting float to int
x = 8.9
print(f"\nint(8.9)       : {int(x)}")

# int() does NOT round the number.
# It truncates the decimal part for positive values.

# Converting string to bool
x = "False"
y = bool(x)
print(f'bool("False")  : {y}')

# Why?
# bool() checks whether the string is empty.
# bool("")      -> False
# bool("False") -> True
# bool("Hello") -> True


# ----------------------------------------------------------------------------
# 4. USER INPUT
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("4. USER INPUT")
print("-" * 72)

# input() always returns a string.
x = input("Enter any value: ")
print(f"You entered    : {x}")
print(f"Input type     : {type(x)}")

# If we want the input as an integer:
number = int(input("Enter an integer: "))
print(f"Integer value  : {number}")
print(f"Integer type   : {type(number)}")


# ----------------------------------------------------------------------------
# 5. BASIC IF STATEMENT
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("5. BASIC IF STATEMENT")
print("-" * 72)

a = 5
b = 67

print(f"a = {a}, b = {b}")

if a < b:
    print("Condition a < b is True")
    print(f"Smaller value  : {a}")

# Parentheses are not required.
# if (a < b): works, but Python style usually prefers:
# if a < b:


# ----------------------------------------------------------------------------
# 6. PRINT SEPARATOR - sep
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("6. PRINT SEPARATOR - sep")
print("-" * 72)

# By default, print() separates multiple values using a space.
print("Default        :", "Hello", "Aman")

# We can change the separator using sep.
print("Colon          :", "Hello", "Aman", sep=":")
print("Languages      :", "Python", "C++", "AI", sep=" | ")


# ----------------------------------------------------------------------------
# 7. PRINT END - end
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("7. PRINT END - end")
print("-" * 72)

# By default, print() ends with \n (new line).
print("Default output:")
print("Hello")
print("Aman")

print("\nUsing end=' ':")
print("Hello", end=" ")
print("Aman")

print("\nUsing custom end:")
print("A", end=" -> ")
print("B", end=" -> ")
print("C")


# ----------------------------------------------------------------------------
# 8. PYTHON REPL
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("8. PYTHON REPL")
print("-" * 72)

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
# When we see >>> it means we are inside the Python REPL.
#
# REPL            -> Quick testing and experiments
# Python .py file -> Complete programs
#
# To run a Python file:
# python Basics.py

print("REPL = Read - Eval - Print - Loop")
print("Use it for quick experiments in the terminal.")


# ----------------------------------------------------------------------------
# 9. OPERATORS
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("9. OPERATORS")
print("-" * 72)

a = 34
b = 2

# ------------------------- ARITHMETIC OPERATORS -------------------------------

print("\n[Arithmetic Operators]")
print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b:<8} -> Addition")
print(f"a - b  = {a - b:<8} -> Subtraction")
print(f"a * b  = {a * b:<8} -> Multiplication")
print(f"a / b  = {a / b:<8} -> Division")
print(f"a % b  = {a % b:<8} -> Modulo / remainder")
print(f"a // b = {a // b:<8} -> Floor division")
print(f"a ** b = {a ** b:<8} -> Exponentiation")

# Normal division always returns a float.
# Floor division rounds down to the nearest integer result.
# Modulo gives the remainder.
# Exponentiation means raising a number to a power.

# ------------------------- COMPARISON OPERATORS -------------------------------

print("\n[Comparison Operators]")
print(f"a == b : {a == b}")
print(f"a != b : {a != b}")
print(f"a > b  : {a > b}")
print(f"a < b  : {a < b}")
print(f"a >= b : {a >= b}")
print(f"a <= b : {a <= b}")

# ------------------------- ASSIGNMENT OPERATORS -------------------------------

print("\n[Assignment Operators]")
x = 10
print(f"Initial x : {x}")

x += 5
print(f"x += 5    : {x}")

x -= 3
print(f"x -= 3    : {x}")

x *= 2
print(f"x *= 2    : {x}")

x /= 4
print(f"x /= 4    : {x}")

x %= 3
print(f"x %= 3    : {x}")

x = 10
x //= 3
print(f"x //= 3   : {x}")

x = 2
x **= 3
print(f"x **= 3   : {x}")

# --------------------------- LOGICAL OPERATORS -------------------------------

print("\n[Logical Operators]")
age = 25
has_license = True

print(f"age >= 18 and has_license : {age >= 18 and has_license}")
print(f"age < 18 or has_license   : {age < 18 or has_license}")
print(f"not has_license           : {not has_license}")

# and -> True only when BOTH conditions are True.
# or  -> True when AT LEAST ONE condition is True.
# not -> Reverses the Boolean value.

# -------------------------- MEMBERSHIP OPERATORS ------------------------------

print("\n[Membership Operators]")
name = "Aman"
numbers = [10, 20, 30, 40]

print(f'"A" in name          : {"A" in name}')
print(f'"z" in name          : {"z" in name}')
print(f'"z" not in name      : {"z" not in name}')
print(f"20 in numbers        : {20 in numbers}")
print(f"100 not in numbers   : {100 not in numbers}")

# --------------------------- IDENTITY OPERATORS -------------------------------

print("\n[Identity Operators]")
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x == y      : {x == y}   -> Values are equal")
print(f"x is y      : {x is y}  -> Different objects")
print(f"x is z      : {x is z}   -> Same object")
print(f"x is not y  : {x is not y}")

# == checks whether VALUES are equal.
# is checks whether both variables refer to the SAME object.

# ---------------------------- BITWISE OPERATORS -------------------------------

print("\n[Bitwise Operators]")
a = 5      # Binary: 0101
b = 3      # Binary: 0011

print(f"a & b  = {a & b}")
print(f"a | b  = {a | b}")
print(f"a ^ b  = {a ^ b}")
print(f"~a     = {~a}")
print(f"a << 1 = {a << 1}")
print(f"a >> 1 = {a >> 1}")


# ----------------------------------------------------------------------------
# 10. IF - ELIF - ELSE STATEMENT
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("10. IF - ELIF - ELSE STATEMENT")
print("-" * 72)

# Important:
# == -> checks whether VALUES are equal
# is -> checks whether both variables refer to the SAME OBJECT
# in -> checks whether a value exists inside a collection
#
# if   -> checks the first condition
# elif -> means "else if"
# else -> runs when all previous conditions are False
#
# Conditions are checked from top to bottom.
# Once one condition is True, the remaining elif/else blocks are skipped.

first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))

x_values = [6, 4, 5, 6, 7, 8, 4]
y_values = [6, 2, 3, 55, 6, 8, 3]

if first_number in [1, 2, 3, 4, 5] and second_number in [6, 7, 8, 9, 10]:
    print("Result: first number is in 1-5 and second number is in 6-10")

elif (
    first_number in x_values
    or second_number in x_values
    or first_number in y_values
    or second_number in y_values
):
    print("Result: at least one number is present in x_values or y_values")

elif first_number >= second_number:
    print(
        f"Result: first number ({first_number}) is greater than or equal to "
        f"second number ({second_number})"
    )

elif first_number < second_number:
    print(
        f"Result: first number ({first_number}) is less than "
        f"second number ({second_number})"
    )

else:
    print("Result: none of the conditions were satisfied")


# ----------------------------------------------------------------------------
# 11. MATCH CASE STATEMENTS
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("11. MATCH CASE STATEMENTS")
print("-" * 72)

month = int(input("Enter a month number (1-12): "))

match month:
    case 1:
        print("Month: January")
    case 2:
        print("Month: February")
    case 3:
        print("Month: March")
    case 4:
        print("Month: April")
    case 5:
        print("Month: May")
    case 6:
        print("Month: June")
    case 7:
        print("Month: July")
    case 8:
        print("Month: August")
    case 9:
        print("Month: September")
    case 10:
        print("Month: October")
    case 11:
        print("Month: November")
    case 12:
        print("Month: December")
    case _:
        print("Invalid month number")


# ----------------------------------------------------------------------------
# 12. FOR LOOPS
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("12. FOR LOOPS")
print("-" * 72)

# Syntax:
# for variable in iterable:
#     statements
#
# Python does not use () or {} around the for-loop block.

print("\n[Basic for loop: range(5)]")
for i in range(5):
    print(i, end=" ")
print()

print("\n[Start and end: range(5, 10)]")
for i in range(5, 10):
    print(i, end=" ")
print()

print("\n[Start, end and step: range(2, 40, 2)]")
for i in range(2, 40, 2):
    print(i, end=" ")
print()

# For loop on a list
fruits = ["Banana", "Mango", "Apple", "Papaya", "Strawberry"]

print("\n\n[Looping directly through a list]")
for this_fruit in fruits:
    print(f"- {this_fruit}")

# For loop on a list with index
print("\n[Looping using range(len(...))]")
n_fruits = len(fruits)

for n in range(n_fruits):
    print(f"Index {n}: {fruits[n]}")

    if fruits[n] == "Apple":
        print(f"Apple found at index {n}. Stopping this loop.")
        break

# For loop using enumerate
print("\n[Looping using enumerate()]")
print("enumerate() gives both index and value.")

for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")


# ----------------------------------------------------------------------------
# 13. WHILE LOOP
# ----------------------------------------------------------------------------

print("\n" + "-" * 72)
print("13. WHILE LOOP")
print("-" * 72)

# Syntax:
# while condition:
#     statements

print("\n[Fruit check using while]")
fruit = input("Enter a fruit: ")

while fruit in fruits:
    print(f'"{fruit}" is already in the list.')
    fruit = input("Enter another fruit: ")

print(f'"{fruit}" is not in the list, so the loop stopped.')

print("\n[Basic counter using while]")
i = 1

while i <= 10:
    print(i, end=" ")
    i += 1

print()


# ============================================================================
#                              END OF PROGRAM
# ============================================================================

print("\n" + "=" * 72)
print("                     BASIC PYTHON RUN COMPLETE")
print("=" * 72 + "\n")
