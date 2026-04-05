first=int(input("Enter the first number:"))
second=int(input("Enter the second number:"))
terms=int(input("Enter the terms:"))

fibo=[first,second]
for i in range(0,terms-2):
    value=fibo[i]+fibo[i+1]
    fibo.append(value)
print(fibo[:terms])    
    
