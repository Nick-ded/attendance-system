attendance = {}  # maps name -> {'present_count': int, 'last_status': str}
total_classes = 0  # total number of times attendance has been marked

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
    # Each call to mark_attendance counts as a new class/session
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

    print("\n--- Attendance (latest status + percentage) ---")
    print(f"Total class sessions marked: {total_classes}")
    for name, data in attendance.items():
        present_count = data['present_count']
        last_status = data['last_status'] or "N/A"
        if total_classes > 0:
            percentage = (present_count / total_classes) * 100
        else:
            percentage = 0.0
        print(f"{name} : {last_status} | {present_count}/{total_classes} classes attended ({percentage:.1f}%)")
    print("----------------------------------------------")

def main():
    while True:
        print("\n===== Attendance Management System =====")
        print("1. Add Student")
        print("2. Mark Attendance (counts as one class/session)")
        print("3. View Attendance + Percentage")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
