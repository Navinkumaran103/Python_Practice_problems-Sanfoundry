#Create a Class which Performs Basic Calculator Operations
class cal():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2    
        

ops=None
while(ops!=0):
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    ops=int(input("Enter the choice:"))
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the Second number:"))
    obj=cal(num1,num2)
    if(ops==1):
        print("Result:", obj.add())
    elif(ops==2):
        
        print("Result:", obj.sub())
    elif(ops==3):
        print("Result:", obj.mul())    
    elif(ops==4):
        print("Result:", obj.div())
    elif(ops==0):
        print("Exiting")
        break
    else:
        print("Invalid choice")
    
    
        
    
