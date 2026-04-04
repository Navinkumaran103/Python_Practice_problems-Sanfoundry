def product(num1,num2):
    if(num1==0 or num2==0):
        return 0
    if num2<0: 
        return -(product(num1, -num2))
    if(num1<0):
        return -(product(-num1, num2))
    
    return(num1+product(num1,num2-1))
      

num1=int(input("ENter the num1:"))
num2=int(input("Enter the num2:"))
print(product(num1,num2))
