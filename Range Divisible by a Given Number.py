lower=int(input("Enter the lower number: "))
upper=int(input("Enter the upper number: "))
num=int(input("Enter the divisible number: "))
if(upper<lower):
    print("Upper should be higher than lower")
else:
    for i in range(lower,upper+1):
        if(i%num==0):
            print(i)
    