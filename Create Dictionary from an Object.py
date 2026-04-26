class Person:
    def __init__(self,name,age):#__init__ is the "construction phase--data injected into __dict__ storage.
        self.name=name 
        self.age=age

name=input("Enter name:")
age=int(input("Enter age:"))
#info=object and person=class
info=Person(name,age)
print(info.__dict__)
