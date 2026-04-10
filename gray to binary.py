n=int(input("Enter the gray: "), 2)
b=0
while n>0:
    b= b^n
    n= n>>1
print(bin(b)[2:])
