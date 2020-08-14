
def add(lst):
    dct = {}
    dct['name'] = input('Enter book name: ')
    dct['author'] =input('Enter books author: ')
    dct['pages'] = input('Enter number of pages: ')
    dct['genre'] = input('Enter genre of the book: ')
    books.append(dct)

def delete(lst, name):
    for index, book in enumerate(lst):
        if book['name'] == name:
            tmp_book = lst.pop(index)
            return tmp_book
    else:
        print('Book ' + name + ' does not exist') 

def search(lst, name):
    for book in lst:
        if book['name'] == name:
            return book
    else:
        print('Book ' + name + ' does not exist')

def change(lst, name):
    for book in lst:
        if book['name'] == name:
            new_name = input('Enter new name: ')
            new_author = input('Enter new author: ')
            new_pages = input('Enter new number of pages: ')
            new_genre = input('Enter new genre: ')
            if new_name:
                book['name'] = new_name
            if new_author:
                book['author'] = new_author
            if new_pages:
                book['pages'] = new_pages
            if new_genre:
                book['genre'] = new_genre
            return book
    else:
        print('Book ' + name + ' does not exist')

def show_library(lst):
    for book in lst:
        for elem, value in book.items():
            print(elem, value, sep=': ')
        print()

if __name__ == '__main__':    

    books = [{'name': 'poi', 'author': 'lkj', 'pages': '200', 'genre': 'mnb'}]
    while True:
        print('\nWhat do you want to do?')
        print('''Enter:
        1 - to see all books\n 
        2 - to add new book\n
        3 - to delete some book\n
        4 - to find some book\n
        5 - to change some information\n
        q - to quit\n'''
        )
        choice = input(' ')
        if choice == 'q':
            break
        elif choice == '1':
            show_library(books)
        elif choice == '2':
            add(books)
        elif choice == '3':
            name = input('Enter the name of book: ')
            delete(books, name)
        elif choice == '4':
            name = input('Enter the name of searching book: ')
            result = search(books, name)
            if result:
                for elem, value in result.items():
                    print(elem, value, sep=': ')
        elif choice == '5':
            name = input('Enter the name of book to change info: ')
            change(books, name)
        else:
            print('You entered something wrong!')
