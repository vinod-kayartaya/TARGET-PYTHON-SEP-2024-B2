import sys
from my_utils import is_float


if __name__ == '__main__':
    args = sys.argv[1:]
    print('the command line arguments are', args)

    nums = [float(arg) for arg in args if is_float(arg)]
    total = sum(nums)
    print(f'{nums = }')
    print(f'{total = }')
