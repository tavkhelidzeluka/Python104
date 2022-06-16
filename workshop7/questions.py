"""
def shekribe(*args: any, key=5, **kwargs) -> float:
    print(type(kwargs), kwargs)
    if len(args) < 2:
        raise Exception('Args must not be empty!')

    s = 0
    for number in args:
        s += number

    return s

print(shekribe(1, 2, key = 5, i=0, g=1))
"""

"""
for i in range(100):
    if i % 2 != 0:
        continue

    if i == 32:
        break

    print(i)
"""

