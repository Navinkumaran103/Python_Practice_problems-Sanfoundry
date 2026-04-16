print("Quadratic equation:ax^2 +bx+c")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

d=(b**2)-(4*a*c)
d1=d**0.5

if d<0:
    print("Root is imaginary")
else:
    r1=(-b+d1)/(2*a) 
    r2=(-b-d1)/(2*a)
    print(r1,r2)    
