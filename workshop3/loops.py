# Loop - ციკლი

# friend_list = ['luka', 'gio', 'nika', 'mari']

# # print(friend_list[0])
# # print(friend_list[1])
# # print(friend_list[2])
# # print(friend_list[3])

# print('Using for loop')

# # Looping through the list
# for friend_name in friend_list:
# 	# escape characters:  \t \n 
# 	print(f'my fried\'s name is:\t{friend_name}')


# numbers: list[int] = [2, 3, 5, 12]

# for number in numbers:
# 	print(f'{number} to the 2nd power: {number ** 2}')
# 	print(f'{number} reminder when divided by 2 {number % 2}')
import time

s = time.time()

a = [_ for _ in range(1_000_000_00)]
# a = []
# for i in range(1_000_000_00):
# 	a.append(i)
# print(a)
print(time.time() - s)