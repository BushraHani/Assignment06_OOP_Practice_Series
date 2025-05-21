#Create a class Department and a class Employee. 
#Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_details(self):
        return f"{self.name} (ID: {self.employee_id})"

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  

    def show_department_info(self):
        print(f"Department: {self.name}")
        print(f"Employee: {self.employee.get_details()}")


emp = Employee("Ali", 101)
dept = Department("HR", emp)

dept.show_department_info()
