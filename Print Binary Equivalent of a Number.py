temp=[]
n=int(input("Enter the number: "))

while(n>0):
    x=n%2
    n=n//2
    temp.append(x)
temp.reverse()
for i in temp:
    print(i, end="")    