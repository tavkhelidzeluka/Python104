# ცვლადი
message = "Hello World!" # Hard Code 
name = "Luka"
age = 21

_my_variable = "niko"

# snake_case; PascalCase; SCREAMING_SNAKE_CASE; camelCase

my_name = "Luka"
# my name  Error
# 5name  Error


n_o_e_i_l = 5 # Bad
number_or_elements_in_list = 5 # Good

f_n = "Joe" # Bad
firs_name = "Joe" # Good

# print(message, name, age)

# String (სიტყვა) str
message = "Hello"
name = "Luka"
# Name = "NIka"
# NaMe = ""
# NAME = ""

# concatenation
# print(message + " " +  name)
# print(f"{message} {name}")
# print("{} {}".format(message, name))
# print(type(name))

message_1 = "Hello {}"
# print(message_1)
# print(message_1.format("Luka"))
# print(f"gamrajoba {name}")

text = "     Lorem ipsum eigneoirugbe uywer  efwef   giwyuerg werg      "

# print(text.strip())
# print(text.rstrip())
# print(text.lstrip())

# print(text.count(" "))
# print(text.title())
# print(text)

# int   - Integer (Z);      (-∞, ..., -2, -1, 0, 1, 2, ..., +∞)
# float - Fraction (Q);     (-∞, ..., -1.12, -1.11, 0, 1.1, 1.12, ... +∞)
# str   - String;           "I'm a String", 'I am a String', """ I'm a String """, ''' I'm a String '''
# bool  - Boolean;          True, False

# "5" ≠ 5

number_1: int = 5
gela = 5

# Addition
# print(number_1 + gela)
# print(5 + 6)
# print(number_1 - gela)
# print(number_1 / gela)
# print(number_1 * gela)
# print(number_1 ** gela)
# print(number_1 // gela)
# print(number_1 % 3)

didi_ricxvi = 1_000_000
# print(didi_ricxvi + 25)

x, y, z = 5, 7, -1
# x = 5
# y = 7
# z = -1
# print(x, z, y)

# constant
ARMY_SIZE_OF_WHITE_CASTLE: int = 1_000_000
# print(ARMY_SIZE_OF_WHITE_CASTLE)

# Bad
ARMY_SIZE_OF_WHITE_CASTLE = "no"

# print(ARMY_SIZE_OF_WHITE_CASTLE)

# Comparison Operators
# >
# <
# <=
# >=
# ==
# !=

name: str = input('Enter your name: ')
# Type Casting
age: int = int( input('Enter your age: ') )
# evaluation
is_adult: bool = age > (4 + 4) * 2 # statement

print(f"Hello I'm {name}, {age} years old, is Adult: {is_adult}")
print(type(age))
