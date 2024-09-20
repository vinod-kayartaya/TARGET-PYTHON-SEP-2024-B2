class Book:
    __CATEGORIES = ['Literature', 'Fantasy', 'Comedy', 'Romance', 'Computers']

    def __init__(self, **kwargs) -> None:
        self.title = kwargs.get('title')
        self.author = kwargs.get('author')
        category = kwargs.get('category')
        if category is not None and category not in Book.__CATEGORIES:
            raise ValueError('Invalid category supplied')
        self.category = category

    @classmethod
    def add_category(cls, category_name):
        Book.__CATEGORIES.append(category_name)
    
    @staticmethod
    def print_categories():
        print('Categories:', ', '.join(Book.__CATEGORIES))
    
    def __str__(self) -> str:
        return f'Book object with title={self.title}, author={self.author} and category={self.category}'

def main():
    Book.add_category('Life skills')

    b1 = Book(title='Let us C', author='Yashwant Kanitkar', category='Computers')
    b2 = Book(title='Python Unleashed', author='John Doe', category='Software Programming')

    print(f'b1 = {b1}')
    print(f'b2 = {b2}')

    Book.print_categories()
    b1.print_categories()

if __name__ == '__main__':
    main()
    
