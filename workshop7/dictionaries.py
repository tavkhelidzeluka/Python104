# Dict | Map

person: dict[str, any] = {
    # key   value pair
    'name': "Niko",
    'age': 18
}

person_2: dict[str, any] = {
    'name': "Luka",
    'age': 21
}

# adding pair
person_2['bobo'] = 18

# updating
person_2['age'] += 1 # person_2['age'] = person_2['age'] + 1

# removing pair
person_2.pop('age')
# del person_2['age']

# person_2.pop('age', None)
# print(person_2['age'])
print(person_2.get('age'))


print(person_2)
print(person['name'])
print(person['age'])


print('\ndefault (Keys)', '-' * 10)

for i in person:
    print(i)
    print(person[i])

print('\nKeys', '-' * 10)

for i in person.keys():
    print(i)
    print(person[i])

# print(person.keys())

print('\nValues', '-' * 10)

for i in person.values():
    print(i)

print('\nBoth (items)', '-' * 10)

for i, v in person.items():
    print(i, '-ზე არის', v)

person.clear()
print(person)

# print(dict.fromkeys(['a', 'b'], [5, 6]))

