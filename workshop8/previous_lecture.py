"""
from typing import Callable, Any


def decor(func: Callable[[], Any]) -> Callable[[], Any]:
    def g() -> Any:
        print(func.__code__.co_varnames)
        return func()

    return g

def upper_case(func):
    def transform(word):
        return func(word).upper()
    
    return transform


@upper_case
def say_hi(word: str):
    return word * 2

@decor
def l(luka = 1, nika = 1):
    return "hi"

print( say_hi('hi') )
"""

# String Method
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent
names = ['luka', 'nika', 'noe']
print(BASE_DIR)

with open(BASE_DIR / 'names.csv', 'w') as f:
    f.write(',\n'.join(names))

