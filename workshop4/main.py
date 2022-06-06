import sys

from copy import copy, deepcopy
from random import randint
from pprint import pprint

# list 
# type hinting | type annotation


workshop_list: list[int] = [1, 2, 3, 4]


# iterate through list | loop though list | გადავლა
for workshop in workshop_list:
    # for block | ციკლის ტანი | Code fragment
    print(workshop)


print()

# a = range(4)
# print(a)

# [0, 4)
for i in range(4):
    print(i)

# [1, 4) step 2
for i in range(1, 4, 2):
    print(i)

print()

# numbers: list[int] = []

# for i in range(100):
#     numbers.append(i)


# list comprehension
numbers: list[int] = [i for i in range(100)] # Correct
# numbers: list[int] = [range(100)] # Wrong
# numbers: list[int] = list(range(100)) # Correct

print(numbers)
print(f'Maximum number in this list is: {max(numbers)}')
print(f'Maximum number in this list is: {min(numbers)}')

print()

# slicing
print(numbers[:10])
print(numbers[5:15])
print(numbers[-5:])
print(numbers[:])
print(numbers[::2])


print()

numbers = [i for i in range(10)]
# numbers_2 = numbers.copy()
# numbers_2 = numbers[:]

# Shallow Copy
numbers_2 = copy(numbers)

numbers_2.append(25)
 
print(numbers)
print(numbers_2)

print()

# numbers = [
#     [randint(0, 1) for _ in range(10)]
#     for _ in range(10)
# ]

# mutable
numbers = [
    [i for i in range(10)]
    for _ in range(3)
]
# Shallow copy
# numbers_2 = numbers[:]
# numbers_2 = numbers.copy()

# Deep Copy
numbers_2 = deepcopy(numbers)

numbers_2[0].append(5)

print('numbers: ', numbers)
print('numbers 2: ', numbers_2)


# immutable | read only
numbers: tuple[int, int, int] = (1, 12, 1)
# empty tuple
# numbers: tuple = ()
print(numbers.count(1))
# numbers[0] = 1
print(numbers)

for number in numbers:
    print(number + 1)

print()
numbers = tuple(range(100))

print(numbers[:5])
print(sys.getsizeof(numbers), sys.getsizeof(list(range(100))))


tuple_of_list = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

tuple_of_list[0][0] = 0
# tuple_of_list[0] = 5
print(tuple_of_list)

print()


