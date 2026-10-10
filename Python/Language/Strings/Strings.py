# ------------------------------------------------------------
# STRINGS IN PYTHON
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. CREATING STRINGS
# ------------------------------------------------------------

name = "Aman"
city = "Pune"

multi_line_string = """This is
a multiline
string"""


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

prefix_name = name[0]
print(prefix_name)          # A

prefix_negative_aman = name[-4]
print(prefix_negative_aman) # A


# ------------------------------------------------------------
# 3. STRINGS ARE IMMUTABLE
# ------------------------------------------------------------

# Strings cannot be modified character by character.

# name[2] = "x"   # ERROR

# If we want to change a string,
# we usually create a new string instead.


# ------------------------------------------------------------
# 4. LENGTH OF A STRING
# ------------------------------------------------------------

# len() returns the number of characters in the string.

print(len(name))            # 4

# ------------------------------------------------------------
# 5. STRING SLICING
# ------------------------------------------------------------

# Syntax:
# string[start : end]
#
# start -> included
# end   -> excluded

sliced_string_name = name[1:4] # man
sliced_string = name[:4] # man


# ------------------------------------------------------------
# 6. STRING SLICING WITH STEP
# ------------------------------------------------------------

# Syntax:
# string[start : end : step]
# P  y  t  h  o  n
# 0  1  2  3  4  5

word = "Python"

print(word[0:6:2])   # Pto

# ------------------------------------------------------------
# 7. STRING METHODS
# ------------------------------------------------------------

# upper()
# Converts all characters to uppercase.

name = "Aman Choudhari"
name_upper = name.upper()
print(name_upper)

# lower()
# Converts all characters to lowercase.

print(name.lower())     # aman choudhari

# capitalize()
# Makes the first character uppercase
# and the remaining characters lowercase.

text = "hello WOrld"
capitalized_text = text.capitalize()     # Hello world
print(capitalized_text)

# title()
# Makes the first letter of every word uppercase.

text = "hello world from python"
print(text.title())         # Hello World From Python


# strip()
# Removes white spaces from the beginning and end of the string only

name = "    Aman    "
name = name.strip()
print(name)


# lstrip()
# Removes white spaces from the left side of the string

left_string = "      Aman"
left_string = left_string.lstrip()
print(left_string)

# rstrip()
# Removes white spaces from the right side of the string 
right_string = "Aman   "
right_string = right_string.strip()
print(right_string)


# replace(old, new)
# Replaces occurrences of old text with new text.

# replace(old, new, count)
# Replaces only the specified number of occurrences.
# If replace() does not find the target string, it simply returns the original string unchanged.

text = "I like python"
new_text = text.replace("python", "C++")
print(new_text)


fruit_str = "apple apple apple apple"
new_fruit_str = fruit_str.replace("apple", "mango", 2)
print(new_fruit_str)





