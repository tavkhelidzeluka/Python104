import sys

# print(sys.argv)
command = sys.argv[-1]
commands = ['start', 'runserver', 'startproject', 'startapp']

if command not in commands:
    raise Exception(f'Available commands: {commands}')

print('Working...')
print('Done!')
