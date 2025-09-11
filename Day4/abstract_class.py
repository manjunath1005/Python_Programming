from abc import ABC, abstractmethod

#Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):             # Abstract method
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
R1=Rectangle(10,20)
print("Area of Rectangle:",R1.area())
C1=Circle(7)
print("Area of Circle:",C1.area())