class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name:",self.name,end=", ")
        print("Salary:",self.salary)

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        super().display()
        print("Department:",self.department)

E1=Employee("Manju",80000)
E1.display()
M1=Manager("Uday",120000,"Sales")
M1.display()