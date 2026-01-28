student = {}

while True:
    print("\n------ STUDENT MANAGEMENT SYSTEM -------\n")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter your choice here: ")

    # 1️⃣ Add Student
    if choice == "1":
        name = input("Enter name: ")
        roll_no = input("Enter roll no: ")
        course = input("Enter course: ")

        student[name] = {"roll_no": roll_no, "course": course}
        print("Student added successfully")

    # 2️⃣ View Students
    elif choice == "2":
        if not student:
            print("Student book is empty")
        else:
            print("\n--- Student List ---")
            for name in student:
                print("Name :", name)
                print("Roll_no:", student[name]["roll_no"])
                print("Course:", student[name]["course"])
                print("-------------------")

    # 3️⃣ Search Student
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in student:
            print("Name :", name)
            print("Roll_no:", student[name]["roll_no"])
            print("Course:", student[name]["course"])
        else:
            print("Student not found")

    # 4️⃣ Delete Student
    elif choice == "4":
        name = input("Enter the name you want to delete: ")
        if name in student:
            student.pop(name)
            print("Student deleted successfully")
        else:
            print("Student not found")

    # 5️⃣ Exit
    elif choice == "5":
        print("thank u for using student management system Goodbye!")
        break

    else:
        print("Invalid choice, please try again")
