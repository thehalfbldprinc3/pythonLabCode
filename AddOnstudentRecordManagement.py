import csv
import os

FILENAME = "students.csv"
FIELDNAMES = ['Roll Number', 'Name', 'Age', 'Course']

# Create the file if it doesn't exist
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

# Add student record
def add_student():
    roll = input("Enter Roll Number: ").strip()
    if student_exists(roll):
        print("Student with this Roll Number already exists.")
        return
    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()
    
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({'Roll Number': roll, 'Name': name, 'Age': age, 'Course': course})
    print("Student added successfully.")

# View all students
def view_students():
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        print(f"\n{'Roll Number':<15}{'Name':<20}{'Age':<10}{'Course':<15}")
        print("-" * 60)
        for row in reader:
            print(f"{row['Roll Number']:<15}{row['Name']:<20}{row['Age']:<10}{row['Course']:<15}")
        print()

# Search for a student
def search_student():
    roll = input("Enter Roll Number to search: ").strip()
    found = False
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Roll Number'] == roll:
                print("Student Found:")
                print(row)
                found = True
                break
    if not found:
        print("Student not found.")

# Update a student's record
def update_student():
    roll = input("Enter Roll Number to update: ").strip()
    updated = False
    students = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Roll Number'] == roll:
                print("Enter new details (leave blank to keep existing):")
                row['Name'] = input(f"New Name [{row['Name']}]: ") or row['Name']
                row['Age'] = input(f"New Age [{row['Age']}]: ") or row['Age']
                row['Course'] = input(f"New Course [{row['Course']}]: ") or row['Course']
                updated = True
            students.append(row)
    
    if updated:
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(students)
        print("Student record updated.")
    else:
        print("Student not found.")

# Delete a student record
def delete_student():
    roll = input("Enter Roll Number to delete: ").strip()
    deleted = False
    students = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Roll Number'] != roll:
                students.append(row)
            else:
                deleted = True
    
    if deleted:
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(students)
        print("Student deleted.")
    else:
        print("Student not found.")

# Check if student exists
def student_exists(roll):
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Roll Number'] == roll:
                return True
    return False

# Menu
def menu():
    init_file()
    while True:
        print("""
STUDENT MANAGEMENT SYSTEM
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()