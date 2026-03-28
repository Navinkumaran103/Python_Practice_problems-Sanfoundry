def check(n):
    if(n<2):
        return n%2==0
    return (check(n-2))    

n=int(input("Enter the number: "))

if check(n)==True:
    print(n, "is even number")
else:
    print(n, "is an odd number")
    
"""    
n=int(input("Enter the number"))
if n&1:
    print(n, "is odd number")
else:
    print(n, "is an even number")
"""    
    