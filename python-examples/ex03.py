from ex02 import say_hello
print(f'Inside the ex03, the value of __name__ is {__name__}')


def entry_func():
    say_hello()

    num = int(input('Enter a number: '))

    if num % 2 == 0:
        print(f'{num} is divisible by 2, and hence it is an even number')
    else:
        print(f'{num} is not divisible by 2, and hence it is an odd number')


if __name__ == '__main__':
    entry_func()
