FILE = "data/records.txt"

def issue_book():
    sid = input("Enter Student ID: ")
    bid = input("Enter Book ID: ")

    if sid == "" or bid == "":
        print("Fields cannot be empty!")
        return

    with open(FILE, "a") as f:
        f.write(f"{sid},{bid},Issued\n")

    print("Book Issued Successfully")


def return_book():
    sid = input("Enter Student ID: ")
    bid = input("Enter Book ID: ")

    if sid == "" or bid == "":
        print("Fields cannot be empty!")
        return

    with open(FILE, "a") as f:
        f.write(f"{sid},{bid},Returned\n")

    print("Book Returned Successfully")


def view_records():
    try:
        with open(FILE, "r") as f:
            data = f.read()

            if data:
                print("\n===== Transaction Records =====")
                print(data)
            else:
                print("No transaction records found")

    except FileNotFoundError:
        print("Records file not found")


def transaction_menu():
    while True:
        print("\n===== TRANSACTION MODULE =====")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View Records")
        print("4. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            issue_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            view_records()
        elif choice == "4":
            break
        else:
            print("Invalid Choice")