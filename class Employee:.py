class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        results = []
        for emp in self.employees:
            if emp.age == age:
                results.append(emp)
        return results

    def search_by_name(self, name):
        results = []
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                results.append(emp)
        return results

    def search_by_salary(self, condition, salary):
        comparison_ops = {
            ">": lambda a, b: a > b,
            "<": lambda a, b: a < b,
            ">=": lambda a, b: a >= b,
            "<=": lambda a, b: a <= b
        }
        results = []
        for emp in self.employees:
            if comparison_ops[condition](emp.salary, salary):
                results.append(emp)
        return results

def main():
    emp_table = EmployeeTable()
    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Parameters:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    search_choice = int(input("Choose a search parameter (1/2/3): "))
    
    if search_choice == 1:
        age = int(input("Enter age to search: "))
        results = emp_table.search_by_age(age)
    elif search_choice == 2:
        name = input("Enter name to search: ")
        results = emp_table.search_by_name(name)
    elif search_choice == 3:
        condition = input("Enter condition (>, <, <=, >=): ")
        salary = int(input("Enter salary to compare: "))
        results = emp_table.search_by_salary(condition, salary)
    else:
        print("Invalid choice")
        return

    if results:
        print("\nSearch Results:")
        for emp in results:
            print(f"Employee ID: {emp.emp_id}")
            print(f"Name: {emp.name}")
            print(f"Age: {emp.age}")
            print(f"Salary: {emp.salary}\n")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
