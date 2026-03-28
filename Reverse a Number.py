n=int(input("Enter the number: "))
num=0
temp=0
reversed_number = int(str(n)[::-1])
while(n>0):
    num=n%10
    n=n//10
    temp=temp*10+num
    
print(temp,reversed_number)    