from ex14 import Laptop


def main():
    l1 = Laptop(make='Apple')
    l1.print()

    # l1.make = 'Apple'  # `make` is a function called as a `setter property`
    l1.model = 'macbook pro'
    l1.price = 156000

    # print(f'{l1.make}')  # here `make` is a function that is a getter property

    l1.print()


if __name__ == '__main__':
    main()
    
