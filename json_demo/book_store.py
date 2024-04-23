from book_operations import get_all_books, create_book
def mainmenu():
    while True:
        choice = input("please enter c for create book, q for quit, l for list: ")
        if choice == "c":
            create_book()
        elif choice == "q":
            exit()
        elif choice == "l":
            get_all_books()
        else:
            print("please enter valid choice")

if __name__ == '__main__':
    mainmenu()