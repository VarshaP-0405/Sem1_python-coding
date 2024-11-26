class Employee:
    def __init__(self,emp_id,emp_name,emp_sal,emp_dept):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_sal=emp_sal
        self.emp_dept=emp_dept
    def emp_assign_department(self, new_department):
        old_department = self.emp_department
        self.emp_department = new_department
        print(f"{self.emp_name} has been reassigned from {old_department} to {new_department}")
    def calculate_emp_salary(self):
         print(f"Salary of {self.emp_name} (ID: {self.emp_id}): {self.emp_salary}")
     def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
        lib=library("Harry Potter","J.K.Rowling")
employees = [
    Employee("Radha", "E7876", 100000, "Developer"),
    Employee("Shiny", "E7499", 45000, "Tester"),
    Employee("David", "E7900", 50000, "Analyst"),
    Employee("Raja", "E7698", 55000, "Designer")
]
for emp in employees:
    emp.print_employee_details()
    emp.calculate_emp_salary()
    print()  
employees[0].emp_assign_department("Team Lead")
print()


employees[0].print_employee_details()
