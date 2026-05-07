#Append, Delete and Display Elements of a List using Classes
class check():
    def __init__(self):
        self.List=[]
    
    def add(self,a):
        return self.List.append(a)
    def delete(self,b):
        return self.List.remove(b)
    def display(self):
        return self.List
            
ops=None
obj=check()
while(ops!=0):
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    ops=int(input("Enter the choice:"))
    if (ops==0):
        print("Exiting")
        break
    if(ops==1):
        num=int(input("Enter the number:"))
        obj.add(num)
        print("Result:", obj.display())
    elif(ops==2):
        num=int(input("Enter the number:"))
        obj.delete(num)
        print("Result:", obj.display())
    elif(ops==3):
        print("Result:", obj.display())    
    else:
        print("Invalid choice")
