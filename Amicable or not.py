def func(num):
    divsum=0
    for i in range(1,num):
        if(num%i==0):
            divsum+=i
    return divsum        


num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))

total1=func(num1)
total2=func(num2)

if(total1==num2 and total2==num1 ):
    print("Amicable")
else:
    print("not Amicable")
   
    
