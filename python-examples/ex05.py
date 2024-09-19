from my_utils import line


def main():
    names = ['vinod', 'shyam']
    print(f'{len(names) = }')
    names.append('vijay')
    print(f'{names = }')
    names.insert(0, 'ajay')
    names.insert(-1, 'james')
    print(f'{names = }')

    i = names.index('shyam')
    print(f'"shaym" is found at index {i} in names')

    if 'vijay' in names:
        names.remove('vijay')

    print(f'{names = }')
    popped_name = names.pop()
    print(f'{popped_name = }, {names = }')

    print(f'{names = }')
    popped_name = names.pop()
    print(f'{popped_name = }, {names = }')

    names.append('vinod')
    c = names.count('vinod')
    print(f'"vinod" appears {c} times in names')


if __name__ == '__main__':
    line()
    main()
    line('=')
