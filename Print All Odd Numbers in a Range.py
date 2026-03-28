lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
if(lower>upper):
    print("Upper limit should be greater than lower limit")
else:
    while lower<=upper:
        if(lower%2!=0):
            print(lower, "\n")
        lower+=1   
