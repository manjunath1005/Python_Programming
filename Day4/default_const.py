class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("Name:",self.name,end=", ")
        print("Roll No:",self.roll_no,end=", ")
        print("Marks:",self.marks,end="\n")

S1=Student("Manuj","21",95)
S2=Student("Uday","22",90)
S1.display()
S2.display()