#    Comparison (Relational) Operators
#    Used to compare two values.

#    == : Equal to
#    != : Not equal to
#    > : Greater than
#    < : Less than
#    >= : Greater than or equal to
#    <= : Less than or equal to

name = input('Enter your name : ')

if name == 'syed':
    print('correct name')
elif name != 'syed':
    print('incorrect name')


num = int(input('Enter a number : '))

if num > 17:
    print('you allow to drive.')
elif num < 18:
    print('you would not allow to drive.')


age = int(input('Enter your age : '))

if age >=7:
    print('namaz is farz on you.')
elif age <=6:
    print('namaz is not farz on you.')