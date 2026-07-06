import re

FILE_NAME = "students.txt"

# Function to validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


# Function to add student
def add_student():
    try:
        name = input("Enter Student Name: ")

        age = int(input("Enter Age: "))
        if age <= 0:
            raise ValueError("Age must be positive.")

        email = input("Enter Email: ")

        if not validate_email(email):
            raise ValueError("Invalid Email Format!")

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{age},{email}\n")

        print("Student Record Saved Successfully!")

    except ValueError as e:
        print("Error:", e)


# Function to read student records
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("No Student Records Found.")
                return

            print("\n----- Student Records -----")
            for record in records:
                name, age, email = record.strip().split(",")
                print("Name :", name)
                print("Age  :", age)
                print("Email:", email)
                print("---------------------------")

    except FileNotFoundError:
        print("No student file found.")


# Main Menu
while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        read_students()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Enter 1, 2 or 3.")
