import time
from threading import Thread, current_thread


def say_hello(name='friend'):
    for _ in range(10):
        print(f'Hello, {name} ({current_thread().name})')
        time.sleep(0.0001)

def greet():
    for _ in range(10):
        print(f'Welcome to Python learning ({current_thread().name})')
        time.sleep(0.0001)

def main():
    # say_hello()
    # greet()

    names = ['Vinod', 'Shyam', 'Suresh']

    # t1 = Thread(target=say_hello, name='custom_thread_1', args=['Vinod'])
    t2 = Thread(target=greet, name='custom_thread_2')
    # t1.start()
    t2.start()

    for each_name in names:
        Thread(target=say_hello, args=[each_name]).start()


    # for _ in range(10):
    #     print(f'Learning concurrency using threads ({current_thread().name})')
    #     time.sleep(0.0001)

    print('end of main()')

if __name__ == '__main__':
    main()