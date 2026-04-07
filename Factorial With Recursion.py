def fact(n):
    if n<=1:
        return 1
    temp=fact(n-1)
    return n*temp

n=int(input("Enter the number:"))
print(fact(n))



