attendance = {}  
total_classes = 0  

# Default login credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

STUDENT_DEFAULT_PASSWORD = "1234"   # all students share this password

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    if name in attendance:
        print("Student already exists!")
    else:
        attendance[name] = {'present_count': 0, 'last_status': None}
        print("Student added.")

def mark_attendance():
    global total_classes
    if not attendance:
        print("No students found!")
        return

    print("\nMark Attendance (y = present, n = absent):")
    total_classes += 1

    for name in attendance:
        while True:
            status = input(f"Is {name} present? (y/n): ").strip().lower()
            if status in ("y", "n"):
                break
            print("Please enter 'y' or 'n'.")

        if status == "y":
            attendance[name]['present_count'] += 1
            attendance[name]['last_status'] = "Present"
        else:
            attendance[name]['last_status'] = "Absent"

    print("Attendance marked successfully!")

def view_attendance():
    if not attendance:
        print("No students found!")
        return

    print("\n--- Full Attendance Summary ---")
    print(f"Total class sessions marked: {total_classes}")

    for name, data in attendance.items():
        present_count = data['present_count']
        last_status = data['last_status'] or "N/A"

        percentage = (present_count / total_classes * 100) if total_classes else 0

        print(f"{name} : {last_status} | {present_count}/{total_classes} classes attended ({percentage:.1f}%)")

    print("----------------------------------------------")

def view_student_attendance(student_name):
    if student_name not in attendance:
        print("Student not found!")
        return

    data = attendance[student_name]
    present_count = data['present_count']
    last_status = data['last_status'] or "N/A"
    percentage = (present_count / total_classes * 100) if total_classes else 0

    print("\n--- Your Attendance ---")
    print(f"Name: {student_name}")
    print(f"Last Status: {last_status}")
    print(f"Present Count: {present_count}/{total_classes}")
    print(f"Attendance Percentage: {percentage:.1f}%")
    print("----------------------------------------------")

def admin_menu():
    while True:
        print("\n===== Admin Menu =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Full Attendance")
        print("4. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Try again.")

def student_menu(student_name):
    while True:
        print(f"\n===== Student Menu ({student_name}) =====")
        print("1. View My Attendance")
        print("2. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_student_attendance(student_name)
        elif choice == "2":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def login():
    print("\n===== Login System =====")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Admin login
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Admin login successful!")
        admin_menu()
        return

    # Student login
    if username in attendance and password == STUDENT_DEFAULT_PASSWORD:
        print("Student login successful!")
        student_menu(username)
        return

    print("Invalid credentials!")

def main():
    while True:
        print("\n===== Main Menu =====")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            login()
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
