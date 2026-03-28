temp=[]
def func(num):
    if(num==0):
        return num
    x=num%2
    func(num//2)
    temp.append(x)
        

n=int(input("enter the number: "))

func(n)

for i in temp:
    print(i, end="")        