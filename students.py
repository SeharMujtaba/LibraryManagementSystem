FILE = "data/students.txt"

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    if sid == "" or name == "":
        print("Fields cannot be empty!")
        return

    with open(FILE, "a") as f:
        f.write(f"{sid},{name}\n")

    print("Student Added Successfully")


def view_students():
    try:
        with open(FILE, "r") as f:
            data = f.read()

            if data:
                print("\nStudent Records:")
                print(data)
            else:
                print("No students found")

    except FileNotFoundError:
        print("Student file not found")


def update_student():
    sid = input("Enter Student ID to update: ")

    try:
        with open(FILE, "r") as f:
            lines = f.readlines()

        found = False

        with open(FILE, "w") as f:
            for line in lines:
                data = line.strip().split(",")

                if data[0] == sid:
                    new_name = input("Enter New Name: ")
                    f.write(f"{sid},{new_name}\n")
                    found = True
                else:
                    f.write(line)

        if found:
            print("Student Updated Successfully")
        else:
            print("Student Not Found")

    except FileNotFoundError:
        print("Student file not found")


def delete_student():
    sid = input("Enter Student ID to delete: ")

    try:
        with open(FILE, "r") as f:
            lines = f.readlines()

        found = False

        with open(FILE, "w") as f:
            for line in lines:
                if not line.startswith(sid + ","):
                    f.write(line)
                else:
                    found = True

        if found:
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")

    except FileNotFoundError:
        print("Student file not found")


def student_menu():
    while True:
        print("\n===== Student Module =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")