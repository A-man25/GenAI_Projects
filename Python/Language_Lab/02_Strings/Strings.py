# ============================================================
#                     STRINGS IN PYTHON
# ============================================================


# ------------------------------------------------------------
# 1. CREATING STRINGS
# ------------------------------------------------------------

name = "Aman"
city = "Pune"

multi_line_string = """This is
a multiline
string"""

print("\n============================================================")
print("1. CREATING STRINGS")
print("============================================================")

print(f"Name : {name}")
print(f"City : {city}")
print(f"\nMultiline String:\n{multi_line_string}")


# ------------------------------------------------------------
# 2. STRING INDEXING
# ------------------------------------------------------------

# Example:
#
#  S  t  r  i  n  g
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1
#
# Positive indexing starts from 0.
# Negative indexing starts from -1 from the end.

print("\n============================================================")
print("2. STRING INDEXING")
print("============================================================")

prefix_name = name[0]
print(f"name[0]  : {prefix_name}")

prefix_negative_aman = name[-4]
print(f"name[-4] : {prefix_negative_aman}")


# ------------------------------------------------------------
# 3. STRINGS ARE IMMUTABLE
# ------------------------------------------------------------

# Strings cannot be modified character by character.

# name[2] = "x"       # ERROR

# If we want to change a string,
# we need to create a new string.

print("\n============================================================")
print("3. STRING IMMUTABILITY")
print("============================================================")

print("Strings cannot be modified character by character.")
print('Example: name[2] = "x" would give an error.')


# ------------------------------------------------------------
# 4. LENGTH OF A STRING
# ------------------------------------------------------------

# len() returns the number of characters in a string.

print("\n============================================================")
print("4. LENGTH OF A STRING")
print("============================================================")

print(f"String : {name}")
print(f"Length : {len(name)}")


# ------------------------------------------------------------
# 5. STRING SLICING
# ------------------------------------------------------------

# Syntax:
#
# string[start:end]
#
# start -> included
# end   -> excluded

word = "Python"

print("\n============================================================")
print("5. STRING SLICING")
print("============================================================")

print(f"Original String : {word}")

print(f"word[0:3]       : {word[0:3]}")
print(f"word[:3]        : {word[:3]}")
print(f"word[3:]        : {word[3:]}")
print(f"word[:]         : {word[:]}")


# ------------------------------------------------------------
# 6. STRING SLICING WITH STEP
# ------------------------------------------------------------

# Syntax:
#
# string[start:end:step]

print("\n============================================================")
print("6. STRING SLICING WITH STEP")
print("============================================================")

print(f"Original String : {word}")
print(f"word[0:6:2]     : {word[0:6:2]}")
print(f"word[::-1]      : {word[::-1]}")

# [::-1] reverses a string.


# ------------------------------------------------------------
# 7. STRING METHODS
# ------------------------------------------------------------

print("\n============================================================")
print("7. STRING METHODS")
print("============================================================")


# ------------------------------------------------------------
# upper() and lower()
# ------------------------------------------------------------

text = "Aman Choudhari"

print("\n--- upper() and lower() ---")

print(f"Original : {text}")
print(f"upper()  : {text.upper()}")
print(f"lower()  : {text.lower()}")

# String methods return a new string.
# They do not modify the original string because
# strings are immutable.


# ------------------------------------------------------------
# capitalize() and title()
# ------------------------------------------------------------

text = "hello WORLD from python"

print("\n--- capitalize() and title() ---")

print(f"Original     : {text}")
print(f"capitalize() : {text.capitalize()}")
print(f"title()      : {text.title()}")

# capitalize()
# -> First character uppercase
# -> Remaining characters lowercase

# title()
# -> First character of every word uppercase


# ------------------------------------------------------------
# strip(), lstrip() and rstrip()
# ------------------------------------------------------------

text = "   Aman Rajesh Choudhari   "

print("\n--- strip(), lstrip() and rstrip() ---")

print(f'Original : "{text}"')
print(f'strip()  : "{text.strip()}"')
print(f'lstrip() : "{text.lstrip()}"')
print(f'rstrip() : "{text.rstrip()}"')

# strip()  -> removes whitespace from both ends
# lstrip() -> removes whitespace from the left
# rstrip() -> removes whitespace from the right
#
# Spaces between words are NOT removed.


# ------------------------------------------------------------
# replace()
# ------------------------------------------------------------

text = "I like Java"

print("\n--- replace() ---")

print(f"Original                  : {text}")
print(f'Replace Java with Python  : {text.replace("Java", "Python")}')

name = "Aman Rajesh Choudhari"

print(f"Original Name             : {name}")
print(f'Replace spaces with "_"   : {name.replace(" ", "_")}')
print(f'Remove all spaces         : {name.replace(" ", "")}')

repeated_text = "apple apple apple"

print(f"\nOriginal                  : {repeated_text}")
print(
    f"Replace first 2 apples    : "
    f'{repeated_text.replace("apple", "mango", 2)}'
)

# Syntax:
#
# string.replace(old, new)
#
# string.replace(old, new, count)
#
# If the old string is not found,
# replace() returns the original string unchanged.


# ------------------------------------------------------------
# find()
# ------------------------------------------------------------

text = "I am learning Python, it's a wonderful language."
word = "wonderful"

# converting it into lower to avoid case mismatch
index = text.lower().find(word.lower())

print("\n--- find() ---")

print(f"Original text   : {text}")
print(f"Searching for   : {word}")

if index != -1:
    print(f"Found at index  : {index}")
else:
    print(f"Result          : Not found")
    print(f"Returned index  : {index}")


# find() searches for a substring inside a string.
#
# It returns:
#   index -> if the substring is found
#   -1    -> if the substring is not found
#
# find() returns the FIRST occurrence.
#
# Syntax:
# string.find(value)
# string.find(value, start)
# string.find(value, start, end)
#
# find() is case-sensitive.
#
# For case-insensitive searching:
# text.lower().find(word.lower())
#
# Use find() when you need the index.
# Use 'in' when you only need True / False.


# ------------------------------------------------------------
# count()
# ------------------------------------------------------------


text = "banana"

print("\n--- count() ---")

print(f"Original text : {text}")
print(f'Count of "a"  : {text.lower().count("a".lower())}')
print(f'Count of "na" : {text.lower().count("na".lower())}')


# count() returns how many times a substring
# appears inside a string.
#
# Syntax:
# string.count(value)
#
# Example:
# "banana".count("a")   -> 3
# "banana".count("na")  -> 2
#
# If the substring is not found,
# count() returns 0.
#
# Example:
# "banana".count("z")   -> 0
# And count() is also case-sensitive.


# ------------------------------------------------------------
# startswith() and endswith()
# ------------------------------------------------------------

text = "Python is amazing !!!"

print("\n--- startswith() and endswith() ---")

str_to_start = "python"
str_to_end = "!"

print(f"Original text              : {text}")
text = text.lower()

print(f'Starts with "{str_to_start}"       : {text.startswith(str_to_start.lower())}')
print(f'Ends with "{str_to_end}"           : {text.endswith(str_to_end.lower())}')

# startswith(value)
# -> checks whether a string starts with a specific value

# endswith(value)
# -> checks whether a string ends with a specific value

# Both return True or False.

# Use case Example filename = "report.pdf"

filename = "report.pdf"

if filename.endswith(".pdf"):
    print("This is a PDF file")


# ------------------------------------------------------------
# split()
# ------------------------------------------------------------

fruit_str = "Apple, Mango, Banana, Orange"

print("\n--- split() ---")

fruit_list = fruit_str.split(", ")

print(f"Original text : {fruit_str}")
print(f"After split   : {fruit_list}")

# split()
# -> breaks a string into parts
# -> returns a list
#
# Syntax:
# string.split(separator)
#
# split() without an argument splits on whitespace.

# cuts the string wherever it finds "<symbol>" and removes that "<symbol>"


# ------------------------------------------------------------
# join()
# ------------------------------------------------------------

fruits = ["Apple", "Mango", "Banana", "Orange"]

print("\n--- join() ---")

text = ", ".join(fruits)

print(f"Original list : {fruits}")
print(f"Joined string : {text}")

# join()
# -> combines multiple strings into one string
#
# Syntax:
# separator.join(iterable)
#
# Usually used with lists of strings.


# ------------------------------------------------------------
# isdigit(), isalpha(), isalnum(), isspace()
# ------------------------------------------------------------

text1 = "12345"
text2 = "Python"
text3 = "Python123"
text4 = "   "

print("\n--- isdigit(), isalpha(), isalnum(), isspace() ---")

print(f'"{text1}" is digit only      : {text1.isdigit()}')
print(f'"{text2}" is alphabet only   : {text2.isalpha()}')
print(f'"{text3}" is alphanumeric    : {text3.isalnum()}')
print(f'"{text4}" is whitespace only : {text4.isspace()}')

# ------------------------------------------------------------
# 8. F-STRINGS
# ------------------------------------------------------------

# f-strings allow variables and expressions
# to be inserted directly inside a string.
#
# Syntax:
# f"text {variable}"

name = "Aman"
age = 25

print(f"My name is {name}")
print(f"My age is {age}")
print(f"Next year I will be {age + 1}")

# Expressions can also be used inside {}


print("\n============================================================")
print("              STRING BASICS COMPLETED")
print("============================================================\n")

# ============================================================
# SUMMARY
# ============================================================

# len(text)              -> length
#
# text[index]            -> character at index
#
# text[start:end]        -> slicing
#
# text[::-1]             -> reverse string
#
# text.upper()           -> uppercase
#
# text.lower()           -> lowercase
#
# text.capitalize()      -> capitalize first character
#
# text.title()           -> title case
#
# text.strip()           -> remove outer whitespace
#
# text.replace(a, b)     -> replace text
#
# text.find(value)       -> find index
#
# text.count(value)      -> count occurrences
#
# text.startswith(x)     -> starts with?
#
# text.endswith(x)       -> ends with?
#
# text.split(x)          -> string to list
#
# x.join(list)           -> list of strings to string
#
# text.isdigit()         -> digits only?
#
# text.isalpha()         -> letters only?
#
# text.isalnum()         -> letters/numbers only?
#
# text.isspace()         -> whitespace only?
#
# "x" in text            -> exists?
#
# "x" not in text        -> does not exist?


# ============================================================
#                      END OF PROGRAM
# ============================================================