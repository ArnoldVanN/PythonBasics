from typing import cast


students = {3 : "Isaac", 2 : "Kenny", 1 : "Judith", 3 : "Pam", 1 : "Lewis", 2 : "Archer"}

while True:
    print("To see a list of commands, type '?'")
    command = input().lower()
    match command:
        case "?":
            print("add: add a student. Usage: add <name> <grade>")
            print("getGrade: gets all students in specified grade. Usage: getGrade <number>")
            print("getAll: gets all students in all grades.")
        case "add":
            name = input("Student Name: ")
            grade = input("Student grade: ")
            students[name] = grade
        case "all":
            for i in sorted (students.keys()) :
                print(i, end = " ")