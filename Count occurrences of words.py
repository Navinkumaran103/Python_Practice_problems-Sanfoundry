#Count occurrences of words
string=input("Enter the strings:")
substring=input("Enter the substring:")
count=0
a=[]
a=string.split(" ")
for i in range(0,len(a)):
    if(substring==a[i]):
        count=count+1

print(count)
