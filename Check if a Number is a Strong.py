n = int(input("Enter the number: "))
num=n
sumd = 0
while(n > 0):
    temp = n % 10
    fact = temp
   
    while(temp > 0):
        if temp==1: break
        temp = temp - 1
        fact =fact * (temp)
    sumd += fact
    n = n // 10
if(num==sumd):
    print(num,"is strong number")
else:
    print(num,"is not strong number")
