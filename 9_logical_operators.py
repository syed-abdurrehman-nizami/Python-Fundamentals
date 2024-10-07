#   Logical Operators
#   Used to combine conditional statements.

#   and : Returns True if both statements are true
#   or : Returns True if one of the statements is true
#   not : Reverses the result, returns False if the result is true


num1 = int(input('Enter a number : '))
num2 = int(input('Enter a number : '))

if num1 == 2 and num2 == 3:
    print('good')
elif num1 == 2 or num2 == 3:
    print('not bad')
else:
    print('bad')

name = input('Enter a name : ')

if not (name == 'syed'):
    print('name is not syed.')
else:
    print('name is syed.')

