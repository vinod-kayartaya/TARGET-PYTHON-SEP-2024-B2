def main():
    nums = [10, 22, 39, 1, 3, 58, 29, 28, 19, 49, 67, 39]
    print(f'{nums = }')
    print(f'{len(nums) = }')
    idx = 5
    print(f'element at index {idx} is {nums[idx]}')
    idx = -7
    print(f'element at index {idx} is {nums[idx]}')
    print(f'{nums[3:8] = }')
    print(f'{nums[3:] = }')
    print(f'{nums[:8] = }')

    print(f'{nums[:] = }')
    print(f'{nums[::1] = }')
    print(f'{nums[::2] = }')
    print(f'{nums[1::2] = }')
    print(f'{nums[::-1] = }')

    # str is equivalent of a list of characters
    my_name = 'vinod kumar'
    print(f'{my_name = }')
    print(f'{my_name[::-1] = }')

if __name__ == '__main__':
    main()
    
