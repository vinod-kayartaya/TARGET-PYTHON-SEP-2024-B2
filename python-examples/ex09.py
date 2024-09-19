from my_utils import line
# useful attributes in a dict:
# 'get', 'items', 'keys', 'pop', 'popitem', 'update', 'values'


def main():

    p1 = {}  # dict
    p1 = dict()
    p1 = {'name': 'Vinod', 'email': 'vinod@vinod.co', 'age': 50, 'married': True}
    p1 = dict(name="Vinod", email='vinod@vinod.co', age=50, married=True)
    p2 = dict(name="John Doe", email='johndoe@xmpl.com', website='www.johndoe.com')

    print(f'{p1 = }')
    print(f'{p1['name'] = }')
    print(f'{p1['email'] = }')
    # print(f'{p1['website'] = }')
    print(f'{p1.get('website', 'no website info') = }')
    print(f'{p2.get('website', 'no website info') = }')
    p1['website'] = 'www.vinod.co'
    print(f'{p1 = }')
    print(f'{p1.keys() = }')
    line()
    for key in p1:
        print(f'{key} --> {p1[key]}')
    
    line()
    for item in p1.items():
        print(f'{item[0]} --> {item[1]}')
    
    line()
    for key, val in p1.items():
        print(f'{key} --> {val}')

if __name__ == '__main__':
    main()
