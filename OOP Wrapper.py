# Base Class
class Employee:
    def __init__(self, name="", age=0, emp_id="", salary=0):
        self.name = name
        self.age = age
        self.__emp_id = emp_id        # private
        self.__salary = salary        # private

    # Getter and Setter
    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)

    def __del__(self):
        print("Employee object deleted")


# Manager Class
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


# Developer Class
class Developer(Employee):
    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language:", self.language)


# Menu Driven Program
emp_list = []

while True:
    print("\n--- Employee Management System ---")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show All Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Name: ")
        age = int(input("Age: "))
        emp_id = input("Employee ID: ")
        salary = int(input("Salary: "))
        e = Employee(name, age, emp_id, salary)
        emp_list.append(e)
        print("Employee Created")

    elif choice == 2:
        name = input("Name: ")
        age = int(input("Age: "))
        emp_id = input("Employee ID: ")
        salary = int(input("Salary: "))
        dept = input("Department: ")
        m = Manager(name, age, emp_id, salary, dept)
        emp_list.append(m)
        print("Manager Created")

    elif choice == 3:
        name = input("Name: ")
        age = int(input("Age: "))
        emp_id = input("Employee ID: ")
        salary = int(input("Salary: "))
        lang = input("Language: ")
        d = Developer(name, age, emp_id, salary, lang)
        emp_list.append(d)
        print("Developer Created")

    elif choice == 4:
        for emp in emp_list:
            print("\n--- Details ---")
            emp.display()

    elif choice == 5:
        print("Exiting system...")
        break

    else:
        print("Invalid choice")
