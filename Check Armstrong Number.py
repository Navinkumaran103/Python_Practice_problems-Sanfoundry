n=int(input("Enter the number:"))
num=n
sumdig=0
while(n>0):
    i=n%10
    sumdig+=i*i*i
    n=n//10
if(sumdig==num):
    print(num,"is Armstrong")
else:
    print(num,"is not Armstrong")
