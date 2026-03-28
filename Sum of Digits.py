num=int(input("Enter the number: "))
dig=0
while(num>0):
   temp=num%10
   num=num//10
   dig=dig+temp
print(dig)   