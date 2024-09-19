def main():
    names = ['vinod', 'Kumar', 'SHYAM', 'Ramesh', 'harish']

    # names_in_uppercase = []
    # for a_name in names:
    #     names_in_uppercase.append(a_name.upper())

    # syntax:
    # new_list = [elem_to_append for elem_to_append in old_list if condition]
    names_in_uppercase = [a_name.upper() for a_name in names]

    print(f'{names = }')
    print(f'{names_in_uppercase = }')

    nums = [12, 23, 34, 55, 67, 89, 39, 29, 199, 1938, 482, 4]
    even_nums = [n for n in nums if n % 2 == 0]
    odd_nums = [n for n in nums if n % 2]

    print(f'{nums = }')
    print(f'{even_nums = }')
    print(f'{odd_nums = }')


if __name__ == '__main__':
    main()
    
