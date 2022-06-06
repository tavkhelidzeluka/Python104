"""
Conditional Operators (პირობითი ოპერატორები)

== - Equality (ტოლობა)
!= - Inequality (უტოლობა)
>  - gt (მეტობა)
<  - lt (ნაკლებობა)
>= - gte (მეტია ან ტოლია)
<= - lte (ნაკლებია ან ტოლია)

Logical Operators (ლოგიკური ოპერატორები)
and
or
not

"""

print(f'{5 == 5 = }') # 5 არის 5 -ის ტოლი? 
print(f'{5 != 5 = }') # 5 არ არის 5 -ის ტოლი?
print(f'5 > 5 = {5 > 5}') # 5 მეტია 5 -ზე?
print(f'{5 < 5 = }') # 5 ნაკლებია 5 -ზე?

#          True     True = True
print(f'{5 == 5 and 6 == 6 = }')  
#          True     True        False = False
print(f'{5 == 5 and 6 == 6 and 8 == 7 = }') 


print(f'{5 == 5 or 8 == 6 or 8 == 7 = }') 
print(f'{6 == 5 or (6 == 6 and 8 == 7) = }')

print(True and True)
print(True and False)


"""
თუ პირობა:
    გააკეთე ეს
თუ არა და:
    გააკეთე ეს
"""

# user = input('enter your user name: ')

# if len(user) < 8:
#     # if block
#     print('Invalid username (username should be > 8)')
# else:
#     # else block
#     print(f'Welcome {user}')

"""
თუ პირობა:
    გააკეთე ეს
თუ არა და პირობა:
    გააკეთ ეს 
თუ არა და პირობა:
    გააკეთ ეს 
თუ არა და პირობა:
    გააკეთ ეს 
თუ არა და:
    გააკეთე ეს
"""

# chaining
# if len(user) < 8:
#     print('Invalid username (username should be > 8)')
#     quit()
# elif len(user) > 12:
#     print('Invalid username (username should be < 12)')
#     quit()
# if user[0].isdigit():
#     # username = 1regheruig -> True
#     # username = eroighenrgf -> False
#     print('Invalid username (username should not start with number)')
#     quit()
# else:
#     print(f'Welcome {user}')

"""
Truthy | Falsy
--------------
1 2 -3 | 0
True   | False
"reg"  | ""
[1, 2] | []
(1. 2) | ()

"""

numbers = []


# if len(numbers) == 0:
#     print('this list is empty')
    
# if not len(numbers):
#     print('this list is empty')

if not numbers:
    print('this list is empty')

# print(not 5 == 5)
