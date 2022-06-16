from pathlib import Path
"""
ფუნქცია, რომელიც მიიღებს მასივს (ლისტს)
და იპოვის უდიდეს რიცხვს 
type hinting!

[1, 2, 3, 4, 5, 6]
"""

"""
# declaration
def find_maximum(L: list[int]) -> int:
    m: int = L[0]
    # for n in L:
    #     if n > m:
    #         m = n
    i: int = 0
    while i < len(L):
        if L[i] > m:
            m = L[i]
        i += 1

    return m

my_numbers = [1, 2, 3, 4, 5, 6]
print(find_maximum(my_numbers))

my_numbers = [12, 24, 35, 14, 35, 6]
print(find_maximum(my_numbers))
"""


class Dog:
    # dunder method
    # constructor
    def __init__(self, name: str, age: int = 0) -> None:
        self.name: str = name  # attribute
        self.age: int = age    # attribute
    
    def roll(self, n: int = 1):
        print(self.name, f'is rolled {n} times')
    
    def speak(self):
        print(self.name, 'is Barking')
    
    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def mate(self, other_dog: 'Dog', *args, **kwargs) -> 'Dog':
        # print(self is other_dog)
        return Dog("new dog")

# class A:
#     pass

# print(A())
my_dog: Dog = Dog("Bobby", 4)  # object / instance
my_other_dog: Dog = Dog(name="Alice", age=3)  # object / instance
my_dog.mate(my_other_dog)
my_dog.mate(my_dog)

my_other_dog.mate(my_dog)

# mate_dog(my_dog, my_other_dog)
# mate_dog(my_other_dog, my_dog)
my_dog.roll()
# Dog.roll(my_dog)
my_dog.speak()
my_other_dog.roll(7)
my_other_dog.speak()


# print(my_dog)
# print(my_other_dog)

# print(f'my dog name is: {my_dog.name}, he/she is {my_dog.age} years old')
# print(f'my other dog\'s name is: {my_other_dog.name}, he/she is {my_other_dog.age} years old')


# my_dog_name = 'Bobby'
# my_dog_age = 4

# friends_dog_name = 'Bobby junior'
# friends_dog_age = 3
BASE_DIR: Path = Path(__file__).resolve().parent
dog_3 = Dog('Meh')

dog_3.mate(my_dog)
# print('\tname')
# print('\nname')
print('-' * 10)
f_path = BASE_DIR / 'data.txt'
f = open(f_path)

name = f.read()
f.seek(0)
names = []
for line in f.readlines():
    if line != '\n':
        names.append(line.strip())
# print(name)
# f.write('egoihugoreu')
print(names)

f.close()

# f = open(f_path, 'w')
with open(f_path, 'w') as f:
    for name in names:
        f.write(name + '\n')

# f.close()


