from random import randint
# While

# i: int = 0
# while i < 8:
#     print(i)
#     # +=; -=; *-; **=
#     # i = i + 1
#     i += 1


# with for loop
# for i in range(8):
#     print(i)


"""

1. ჩაიფიქრა რიცხვი
2. და მომხმარებელმა უნდა გამოიცნოს
    2.1  მომხმარებელმა თამაშის დასრულებამდე შემოიტანოს რიცხვი

თუ მომხმარებლის მიერ შემოტანილი რიცხვი მეტია ჩაფიქრებულზე უნდა დაიწეროს მეტია
თუ ნაკლებია, ნაკლებია

"""
# boilerplate

"""
number: int = randint(0, 100)
print(number)

while True:
    user_guess: int = int(input('Enter number: '))
    print(user_guess)
    if user_guess < number:
        print("Less!")
    elif user_guess > number:
        print("Greater!")
    else:
        print("Correct! You guessed the number!")
        break

"""

"""
for i in range(7000):
    if i == 50:
        print(i)
        break
"""

"""
number: int = randint(0, 100)
print(number)
running: bool = True

while running:
    user_guess: int = int(input('Enter number: '))
    print(user_guess)
    if user_guess < number:
        print("Less!")
    elif user_guess > number:
        print("Greater!")
    else:
        print("Correct! You guessed the number!")
        running = False
"""

"""
number: int = randint(0, 100)
print(number)

while True:
    user_guess: int = int(input('Enter number: '))
    print(user_guess)

    if user_guess < number:
        print("Less!")
        continue
    if user_guess > number:
        print("Greater!")
        continue

    print("Correct! You guessed the number!")
    break
"""
"""

random_numbers: list[int] = [randint(0, 100) for _ in range(2)]
is_even: bool = False
print(random_numbers)

for number in random_numbers:
    if not number % 2:
        print('even')
        is_even = True
        break
else:
    print('odd')

# if not is_even:
#     print('odd')
# else:
#     print('odd')

"""
"""
def func():
    print("Hello from func")


# function call
func()

"""
"""
# arbitrary / positional parameters
def jami(a, b):
    print(a + b)

def gayofa(a, b):
    print(a / b)

# arguments
jami(5, 6)

gayofa(0, 2)

"""
# None
# def jami(a, b):
#     print(a + b)
"""
def jami(a: int | float, b: int | float) -> int | float:
    return a + b

j = jami(5, 6)
# j = jami(True, "World")

# print(int(.9 + .1))

print(j)

"""
"""
# non arbitrary | default value
def function_with_default_values(name: str, greeting_sentence: str = "Hello") -> None:
    print(f'{greeting_sentence} {name}')

function_with_default_values("Luka")
function_with_default_values("Nika", "Hallo")
function_with_default_values("Mari", "მოგესალმები")
function_with_default_values("Mari", greeting_sentence="მოგესალმები")
function_with_default_values(name="Mari", greeting_sentence="მოგესალმები")

# print(5, 6, 7, 8, sep='')

"""


def jami(a: int | float, *args) -> int | float:
    print(args)
    return

# print([1, 2, 3, 4])
# print(*[1, 2, 3, 4]) # print(1, 2, 3, 4)


# jami(1, 2, 3, 4, 5)
# jami(1)

"""
def func(a = 1, *args, name="luka", **kwargs):
    print(f'{a = }; {name = }')
    print(args)
    print(kwargs)


# func(2, 6, True, False, "Nika", "Gela", [1, 2, 3], b=5, c=30, k="Gela")
func(5, 6, 7, 8, "luka", name="Nika", ages=5)

"""

# def func(*, name: str = "Luka", age: int = 21):
#     print(name, age)

# func(name=345)

# def func(a, b):
#     print(a, b)

# func(a= 5, b =7)
"""
# unpacking / destructuring
def func(a, b):
    return a + b, b * a

x, y = func(5, 6)

print(y + 7)
"""