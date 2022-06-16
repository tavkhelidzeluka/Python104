class Person:
    # __slots__ = 'name', 'age'
    count = 0 # static attribute

    @staticmethod
    def test():
        print('Static method')

    @staticmethod
    def increase_count() -> None:
        Person.count += 1

    def __init__(self, name: str, age: int) -> None:
        # initialize | constructor
        self.name = name
        self.age = age
        # self.count = self.count + 1
        Person.count += 1
        # Person.increase_count()
    
    # dunder method | magic
    def __str__(self) -> str:
        return self.name
    
    def __del__(self):
        # destuctor
        print(self.name, 'object was destroyed!')
        Person.count -= 1


person = Person("p", 17)
person.jemali = 5
print(person.jemali)
print(person.count)
person2 = Person("p1", 14)
print(Person.count)

person3 = Person("p2", 87)
print(person.count)


print(person)

del person
print(Person.count)
Person.test()
person2.test()

# print(Person.count)
