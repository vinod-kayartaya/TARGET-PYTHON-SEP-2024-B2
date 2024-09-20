from threading import Thread, current_thread, Lock
import time

lock = Lock()

def to_words(s:str, words: list)->None:
    print(f'returning from to_words() of {current_thread().name}')
    for _ in range(10):
        print(f'Hello, world ({current_thread().name})')
        time.sleep(0.05)

    lock.acquire()
    for a_word in s.split(' '):
        words.append(a_word)
        time.sleep(0.05)
    lock.release()

def play_music():
    while True:
        print('la la...', end='', flush=True)
        time.sleep(0.05)

def main():
    words = []  # mutable shared resource (with 2 threads)
    s1 = 'my name is vinod and i live in bangalore'
    s2 = 'the quick brown fox jumps over the lazy dog'

    t1 = Thread(target=to_words, args=(s1, words))
    t2 = Thread(target=to_words, args=(s2, words))
    # t3 = Thread(target=play_music, daemon=True)
    # t3.daemon = True

    t1.start()
    t2.start()
    # t3.start()
    
    t1.join()
    t2.join()

    print(f'{words = }')
    print('End of main()')


if __name__ == '__main__':
    main()
    
