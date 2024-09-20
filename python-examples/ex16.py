def box(fn):
    # if this is a decorator, then this should return another function
    # also can invoke the `fn``

    def wrapper(*args, **kwargs):
        print('----------------')
        fn(*args, **kwargs)
        print('----------------')

    return wrapper

def repeat(n=2):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fn(*args, **kwargs)
        return wrapper
    return decorator

@box
@repeat(10)
def say_hello(name='world'):
    print(f'Hello, {name}!')


def main():
    say_hello('Vinod')


if __name__ == '__main__':
    main()
    
