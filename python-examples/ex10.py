from pprint import pprint
from my_utils import create_dict, print_json


def main():
    column_names = ['id', 'name', 'dept', 'salary', 'email', 'grade', 'promotion_due']
    column_values = [929, 'Ramesh', 'Accounting', 45000, 'ramesh.iyer@xmpl.com', 'B+', True]

    emp1 = create_dict(column_names, column_values)
    pprint(emp1)
    print_json(emp1, indent=3)


if __name__ == '__main__':
    main()
    
