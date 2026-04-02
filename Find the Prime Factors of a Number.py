def isprime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True    
n=int(input("Enter the number:"))

for i in range(1,n+1):
    if(n%i)==0:
        if(isprime(i)):
            print(i)

            
# in problems like this divide the problem logic in this case: we need to get factors and check if prime          
   
