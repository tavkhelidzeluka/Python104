# decorators
from typing import Callable

def plus_one(func):
    def wrapper(x: int):
        return func(x) + 1
    
    return wrapper


@plus_one
def increase(x: int) -> int:
    return x + 1


@plus_one
def decrease(x: int) -> int:
    return x - 2
# plus_one = lambda x: increase(x) + 1

# print(plus_one(5), increase(5))

# print(increase(5), decrease(5))
# print(
#     plus_one(increase)(5)
# )

def to_upper(func: Callable[[], str]):
    def wrapper(*args):
        return func(*args).upper()
    
    return wrapper

def split_word(func: Callable[[], str]):
    def wrapper(*args):
        return func(*args).split()
    
    return wrapper


@split_word
@to_upper
def everything_to_upper(*args) -> str:
    return ' '.join(args)

# print(say_hi())
# print('-'.join(['luka','nika','hello']))


a = ["regger ", "ergegiurhg ", "ergiuegpeui"]

print(everything_to_upper(*a))
