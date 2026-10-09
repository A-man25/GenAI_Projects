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
