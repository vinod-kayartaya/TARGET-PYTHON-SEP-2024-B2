def say_hello():
    """
    This function prints a decorated hello world message.
    """

    print(' ----------------')
    print('| Hello, world!  |')
    print(' ----------------')


def main():
    say_hello()

    user_name = input('Enter your name: ')
    user_age = int(input('Enter your age: '))

    print(user_name + ' is ' + str(user_age) + ' years old.')
    print('%s is %d years old.' % (user_name, user_age))
    print('{} is {} years old.'.format(user_name, user_age))

    print(f'{user_name} is {user_age} years old.')

    print(f'{user_name = }')
    print(f'{user_age = }')
    print(f'person_name : {user_name}')
    print(f'user_age : {user_age}')


print(f'Inside the ex02, the value of __name__ is {__name__}')
# execute this section only if you are execuing this file (and not importing the file)
if __name__ == '__main__':
    main()
