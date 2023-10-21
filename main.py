from time import sleep
import json
import os

library = [{'Title': 'Metro', 'Author': 'Dima', 'Year': '2013', 'Genre': 'Roman', 'Status': '3'},
           {'Title': 'Aetro', 'Author': 'Dima', 'Year': '2023', 'Genre': 'Xoman', 'Status': '1'},
           {'Title': 'Aetro', 'Author': 'Vasya', 'Year': '2023', 'Genre': 'Xoman', 'Status': '1'},
           {'Title': 'Aetro', 'Author': 'Vasya', 'Year': '2023', 'Genre': 'Xoman', 'Status': '1'}]


def user_input(txt=': '):
    return input(txt)


def add_book():
    sleep(1)
    print('To add a book, we need some info about this book:')
    book = {
        "Title": user_input('Enter a title name: '),
        "Author": user_input('Enter author: '),
        "Year": user_input('Enter year: '),
        "Genre": user_input('Enter genre: '),
        'Status': user_input('Enter status (Read, Reading, To read): ')
    }

    if book not in library:
        library.append(book)
        print('Book added')
    else:
        sleep(1)
        print("Book already in librabry")


def modify_book():
    print('To modify a book from the library, we need to get information about the book.')
    title_to_remove = user_input('Enter the title of the book to modify: ').capitalize()
    author_to_remove = user_input('Enter the author of the book to modify: ').capitalize()
    found = [book for book in library if book['Title'] == title_to_remove and book['Author'] == author_to_remove]
    print('You can modify reading status or genre')
    print('To mofidy reading status enter 2')
    print('Else 1')
    command = user_input()
    if command == '1':
        for book in found:
            book['Genre'] = user_input('Enter new value for Genre')
    elif command == '2':
        for book in found:
            try:
                book['Status'] = user_input('Enter new value for Status')
            except ValueError:
                print("Error try again")


def search_book():
    print('You can search book by title, author, genre, or reading status.')
    command = user_input('Enter searching option ').lower()
    if command == 'title':
        searching = user_input('Enter title: ').capitalize()
        found_sigments = [book for book in library if book['Title'] == searching]

        if found_sigments:
            for book in found_sigments:
                print(book)
        else:
            print("No books from this author")
        return found_sigments
    if command == 'author':
        searching = user_input('Enter author: ').capitalize()
        found_sigments = [book for book in library if book['Author'] == searching]

        if found_sigments:
            for book in found_sigments:
                print(book)
        else:
            print("No books from this author")
        return found_sigments

    if command == 'genre':
        searching = user_input('Enter genre: ').capitalize()
        found_sigments = [book for book in library if book['Genre'] == searching]

        if found_sigments:

            for book in found_sigments:
                print(book)
        else:
            print("No books with this genre")
        return found_sigments

    if command == 'reading status':
        searching = user_input('Enter reading status: ').capitalize()
        found_sigments = [book for book in library if book['Status'] == searching]

        if found_sigments:
            for book in found_sigments:
                print(book)
        else:
            print("No books with this status")
        return found_sigments


def remove_book():
    print('To remove a book from the library, we need to get information about the book.')
    title_to_remove = user_input('Enter the title of the book to remove: ').capitalize()
    author_to_remove = user_input('Enter the author of the book to remove: ').capitalize()

    indexes_to_remove = [index for index, book in enumerate(library) if
                         book['Title'] == title_to_remove and book['Author'] == author_to_remove]
    if indexes_to_remove:
        indexes_to_remove.reverse()
        for index in indexes_to_remove:
            removed_book = library.pop(index)
            print(f'Book removed: {removed_book}')
    else:
        print('No matching book found for removal')


def display_library():
    print('We will display all library')
    for book in library:
        for key, value in book.items():
            print(f'{key} : {value}')
            print("-" * 20)
        print('=' * 20)


def save_library():
    file_path = 'library.json'
    with open(file_path, 'w') as file:
        json.dump(library, file)


def load_library():
    global library
    file_path = r'C:\Users\PersonalLibraryManager\library.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            library = json.load(file)
    else:
        print('No saved library found.')


def greet():
    print(f'Hello and welcome in our product called: Personal Library Manager or PLM')
    sleep(1)
    print("You will see full menu in couple of seconds")
    sleep(1)


def goodbye():
    print('Goodbye user, we will w8 you back again')


def user_menu():
    flag = True
    greet()
    while flag:
        print('You have 7 options')
        sleep(1)
        print('1: Add a book')
        print('2: Modify book info')
        print('3: Search for a book')
        print('4: Remove a book')
        print('5: Display all library')
        print('6: Save and load library')
        print('7: Exit')
        sleep(1)
        print('To enter a command input number of a command')
        command = user_input()
        if command == "1":
            add_book()
        if command == "2":
            modify_book()
        if command == "3":
            search_book()
        if command == "4":
            remove_book()
        if command == "5":
            display_library()
        if command == "6":
            print("1: if you want to save all data")
            print("2: if you want to upload data")
            user_choice = user_input()
            if user_choice == "1":
                save_library()
            elif user_choice == "2":
                load_library()

        if command == '7':
            goodbye()
            flag = False


def main():
    user_menu()


if __name__ == '__main__':
    main()
