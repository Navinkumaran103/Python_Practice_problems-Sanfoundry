n=int(input("Enter the number:"))
num=n
sumdig=0
for i in range(1,n):
    if(n%i==0):
       sumdig+=i
if(sumdig==num):
    print(num,"It is perfect num")
else:
    print(num,"It is not perfect num")