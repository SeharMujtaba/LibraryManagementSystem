FILE = "data/books.txt"

def add_book():
    bid = input("Enter Book ID: ")
    title = input("Enter Book Title: ")

    if bid == "" or title == "":
        print("Fields cannot be empty!")
        return

    with open(FILE, "a") as f:
        f.write(f"{bid},{title}\n")

    print("Book Added Successfully")


def view_books():
    try:
        with open(FILE, "r") as f:
            data = f.read()

            if data:
                print("\n===== Book Records =====")
                print(data)
            else:
                print("No books found")

    except FileNotFoundError:
        print("Book file not found")


def update_book():
    bid = input("Enter Book ID to update: ")

    try:
        with open(FILE, "r") as f:
            lines = f.readlines()

        found = False

        with open(FILE, "w") as f:
            for line in lines:
                data = line.strip().split(",")

                if data[0] == bid:
                    new_title = input("Enter New Title: ")
                    f.write(f"{bid},{new_title}\n")
                    found = True
                else:
                    f.write(line)

        if found:
            print("Book Updated Successfully")
        else:
            print("Book Not Found")

    except FileNotFoundError:
        print("Book file not found")


def delete_book():
    bid = input("Enter Book ID to delete: ")

    try:
        with open(FILE, "r") as f:
            lines = f.readlines()

        found = False

        with open(FILE, "w") as f:
            for line in lines:
                if not line.startswith(bid + ","):
                    f.write(line)
                else:
                    found = True

        if found:
            print("Book Deleted Successfully")
        else:
            print("Book Not Found")

    except FileNotFoundError:
        print("Book file not found")


def book_menu():
    while True:
        print("\n===== BOOK MODULE =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")