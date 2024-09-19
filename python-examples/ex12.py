import json
import time


def main():
    filename = input('Enter CSV filename: ')
    if not filename.endswith('.csv'):
        raise ValueError('file must be a csv file')

    # file = open(filename, encoding='utf-8')
    with open(filename, encoding='utf-8') as file:
        # while exiting this block, file.close() is automatically called

        # read the first line (header)
        header = file.readline().strip().split(',')
        emp_list = []
        for line in file:
            values = line.strip().split(',')
            values = [
                int(each_value) if each_value.isnumeric() else each_value
                for each_value in values
            ]
            emp = dict(zip(header, values))
            emp_list.append(emp)

        json_filename = f'{filename[:-4]}_{str(time.time()).replace('.', '_')}.json'
        with open(json_filename, 'wt') as file2:
            json.dump(emp_list, file2)
            print(f'{filename} is now saved in JSON format in {json_filename}')


if __name__ == '__main__':
    main()
    
