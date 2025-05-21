#Create a class Employee with:
#a public variable name,
#a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        
        self._salary = salary   
        self.__ssn = ssn        


emp = Employee("Ali", 50000, "123-45-6789")

print(emp.name)  
print(emp._salary)  


print(emp._Employee__ssn)  
