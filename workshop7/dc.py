from dataclasses import dataclass
import sys

@dataclass
class Person:
    name: str
    age: int



p = Person("luka", "nika")
print(p)
