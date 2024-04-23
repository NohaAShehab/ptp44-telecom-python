
from file_handler import read_data_from_json, save_data_to_json
from inputs_module import  ask_for_int, ask_for_string, generate_id_from_file
def get_all_books():
    books = read_data_from_json("books.json")
    if books:
        for book in books:
            print(book)
    else:
        print("--- No books yet ")


def create_book():
    title = ask_for_string("Please enter book title: ")
    pages = ask_for_int("Please enter number of pages: ")
    id = generate_id_from_file()
    book= {
        'id': id,
        'title': title,
        'pages': pages
    }
    print(book)
    saved = save_data_to_json( 'books.json', book)
    print(saved)
