div=[]
i=2
n=int(input("Enter the number: "))
while(n>=i):
    if(n%i==0):
        print(i)
        div.append(i)
    i+=1
div.sort()    
print(div[0])    