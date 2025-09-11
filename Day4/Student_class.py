class Student:
    name=""
    roll_no=""
    marks=0
    def display(self):
        print("Name:",self.name,end=", ")
        print("Roll No:",self.roll_no,end=", ")
        print("Marks:",self.marks,end="\n")

S1=Student()
S1.name="Manju"
S1.roll_no="21"
S1.marks=95
S2=Student()
S2.name="Uday"
S2.roll_no="22"
S2.marks=90
S1.display()
S2.display()
