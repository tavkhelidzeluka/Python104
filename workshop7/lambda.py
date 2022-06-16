# lambda | anonymous | inline

import random

# def my_sort_key(x):
#     # first class citizen
#     return -x


print(
    sorted([random.randint(1, 100) for _ in range(10)], key=lambda x: x)
)
