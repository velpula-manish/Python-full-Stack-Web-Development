# Employee Management System with File Storage
import json
import os

# File to store employee data
DATA_FILE = "employees.txt"

# Initialize employee list
employees = []

def load_employees():
    """Load employee data from the text file."""
    global employees
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                employees = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error loading data. Starting with empty employee list.")
            employees = []
    else:
        employees = []

def save_employees():
    """Save employee data to the text file."""
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(employees, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def create_employee():
    print("\n--- Create Employee ---")
    name = input("1. Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("2. Enter your age (18-60): "))
        if not 18 <= age <= 60:
            print("Age must be between 18 and 60.")
            return
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    designation = input("3. Enter your designation (Project Manager/Manager/Tester): ").strip().lower()
    salary_map = {"project manager": 25, "manager": 30, "tester": 20}
    if designation not in salary_map:
        print("Invalid designation. Choose Project Manager, Manager, or Tester.")
        return
    salary = salary_map[designation]

    confirm = input("Save this employee record? (Yes/No): ").strip().lower()
    if confirm == "yes":
        employees.append({"name": name, "age": age, "designation": designation.title(), "salary": salary})
        save_employees()
        print("Employee record saved successfully!")
    else:
        print("Employee record not saved.")

def display_employees():
    print("\n--- Employee Records ---")
    if not employees:
        print("No employee records found.")
        return
    print("Name\tAge\tSalary\tDesignation")
    print("-" * 40)
    for emp in employees:
        print(f"{emp['name']}\t{emp['age']}\t${emp['salary']}\t{emp['designation']}")

def raise_salary():
    print("\n--- Raise Salary ---")
    if not employees:
        print("No employee records found.")
        return
    name = input("Enter the name of the employee: ").strip()
    for emp in employees:
        if emp["name"].lower() == name.lower():
            try:
                percentage = float(input("Enter percentage hike (max 30%): "))
                if not 0 <= percentage <= 30:
                    print("Percentage must be between 0 and 30.")
                    return
                emp["salary"] = round(emp["salary"] * (1 + percentage / 100), 2)
                save_employees()
                print(f"Salary updated successfully! New salary for {emp['name']}: ${emp['salary']}")
                return
            except ValueError:
                print("Invalid percentage. Please enter a number.")
                return
    print("Employee not found.")

def main():
    # Load employees from file at startup
    load_employees()
    
    while True:
        print("\n=== Employee Management System ===")
        print("1. Create")
        print("2. Display")
        print("3. Raise Salary")
        print("4. Exit")
        try:
            choice = input("Enter your choice (1-4): ").strip()
            if choice == "1":
                create_employee()
            elif choice == "2":
                display_employees()
            elif choice == "3":
                raise_salary()
            elif choice == "4":
                print("\nThank you for using Applications")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except KeyboardInterrupt:
            print("\nPlease enter a valid choice.")
            continue

if __name__ == "__main__":
    main()