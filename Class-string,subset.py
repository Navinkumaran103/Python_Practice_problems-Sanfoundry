#Create a Class in which One Method Accepts a String from the User and Another Prints it
class stringname():
    def __init__(self):
        self.text=""
    def stringget(self):
        self.text=input("Enter the string:")
    def stringprint(self):
        print(self.text)

obj=stringname()  
obj.stringget()
obj.stringprint()
    
#Create a Class and Get All Possible Distinct Subsets from a Set
class subset():
    def f1(self,s):
        return self.f2([], sorted(s))
    def f2(self, current, remaining):
        if not remaining:
            return [current]
        
        include=self.f2(current + [remaining[0]],remaining[1:])
        exclude=self.f2(current,remaining[1:])
        #return include+exclude
        


a=[]
n=int(input("Enter the number elements:"))
for i in range(0,n):
    b=int(input("Enter the numbers:"))
    a.append(b)
print(subset().f1(a))    

