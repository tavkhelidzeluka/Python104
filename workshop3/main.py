# Data Structures: List, Tuple

# name_1: str = "nika"
# name_2: str = "noe"
# name_3: str = "Nino"

# array <=> list
from distutils.command.build_scripts import first_line_re


friend_list = ["Nika", "Elene", "Gio", "Irakli", "Elena"]

print(friend_list)

# index
# print(friend_list[0])
# print(friend_list[1])
# print(friend_list[2])
# print(friend_list[3])

friend_list.append("Mari")
print(friend_list)
friend_list.append("James")
print(friend_list)
friend_list.pop()
print(friend_list)

# Assignment 
friend_list[3] = "Alexander"
# print(friend_list)
# print(friend_list[3])

# friend_list[7]
# Recently added friend
# print(friend_list[4])
# print(f'I have {len(friend_list)} friends')
# print(friend_list[2 + 2])

friend_list.append("Bill")
print(friend_list)
# hard coded 
# print(f'Recently added friend is {friend_list[4]}')

# dynamic (computed)
# print(f'Recently added friend is {friend_list[len(friend_list) - 1]}')

# negative indexes
print(f'Recently added friend is {friend_list[-1]}')
# index error
# print(f'Recently added friend is {friend_list[-7]}')
# print(f'first element calculated from last element {friend_list[-len(friend_list)]}') # Noe + 

# friend_list.pop(2)
del friend_list[5]

# friend_list.pop(5)
print(friend_list)
# friend_list.clear()
# print(friend_list)
print('Sorting')
friend_list.sort()
# keyword argument
# friend_list.sort(reverse=True)
print(friend_list)

# name: str = "luka"
# print(name)
# del name

# print(name)

# numbers = [23, 4, -6, 11, -23]
# print(numbers)
# numbers.sort()
# print(numbers)

