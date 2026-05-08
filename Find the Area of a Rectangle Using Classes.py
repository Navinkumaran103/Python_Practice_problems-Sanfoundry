#Find the Area of a Rectangle Using Classes
class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth       
    def area(self):
        return self.length * self.breadth
 
length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
obj=rectangle(length,breadth)  
print("Result:", obj.area())
