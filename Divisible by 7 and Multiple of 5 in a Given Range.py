lower=int(input("Enter the number: "))
upper=int(input("Enter the number: "))
if(upper<lower):
    print("Upper should be higher than lower")
else:
    for i in range(lower,upper):
        if(i%7==0 and i%5==0):
            print(i)