"""
Example of using `while` and `for` loops

`while` loop is used when the number of iterations is not known
`for` loop is used:
    - we know the number of iterations; use the range object
    - iteration over collections
"""


def while_loop_demo():
    """
    An exampole of a while loop
    """
    upper_limit = int(input('Enter upper limit: '))
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    a, b = 0, 1

    while True:
        c = a + b
        if c > upper_limit:
            break
        a, b = b, c

    print(f'Largest fibonacci element under {upper_limit} is {b}.')


def for_loop_demo_1():
    """
    An example of a for loop using range object
    """
    try:
        num = int(input('Enter a number: '))
        for i in range(1, 11):
            print(f'{num} X {i} = {num*i}')
    except ValueError:
        print('You must try with a number only.')


def fibo(n= 10):
    """
    represents an iterable of `n` number of fibonacci elements 
    """
    fib_nums = []
    a, b = -1, 1
    for _ in range(n):
        c = a + b
        a, b = b, c
        print(f'appending {c}...')
        fib_nums.append(c)

    return fib_nums


def generate_fibo(n=10):
    """
    represents a generator of `n` number fibonacci elements.
    """
    a, b = -1, 1
    for _ in range(n):
        c = a + b
        a, b = b, c
        yield c

    return 100

def generator_demo():
    """
    demo on using generators
    """
    # for i in generate_fibo(20):
    #     print(f'{i}', end=', ')
    # print()

    f = generate_fibo(20)
    print(f'{type(f) = }')

    print(f'{next(f) = }')
    print(f'{next(f) = }')
    print(f'{next(f) = }')
    print(f'{next(f) = }')


def test_gen():
    print('pass-1')
    yield 1
    print('pass-2')
    yield 2
    print('pass-3')
    yield 3
    print('pass-4')
    yield 4



def main():
    """
    Entry point simulation
    """
    # while_loop_demo()
    # for_loop_demo_1()
    # generator_demo()

    g = test_gen()
    # while True:
    #     try:
    #         print(next(g))
    #     except StopIteration:
    #         break

    for i in g:
        print(i)

if __name__ == '__main__':
    main()
