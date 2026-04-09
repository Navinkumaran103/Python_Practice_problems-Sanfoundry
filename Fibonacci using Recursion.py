def fib(first,Second,n):
    if n==0:
        return 
    print(first, end=" ")    
    total=first+Second    
    fib(Second,total,n-1)
    


first=int(input("Enter the number:"))
Second=int(input("Enter the number:"))
n=int(input("Enter the number:"))

fib(first,Second,n)


"""
Void Functions: Not every function needs to return a mathematical value. 
When the primary goal is an action (like printing or logging), 
the 'return' statement acts purely as a 'Stop' signal for the recursion, 
ensuring the function exits the stack without passing back data.
"""    
