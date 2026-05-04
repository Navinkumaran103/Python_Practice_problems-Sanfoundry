#Count the Frequency of Each Word in a String using Dictionary
string=input("Enter the string:")
word=string.split(" ")
d={}
for w in word:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
print(d)    

#generate a dictionary that contains numbers (between 1 and n) in the form (x,x*x).
n=int(input("Enter the limit:"))
d={}
for x in range(0,n+1):
    d[x]=x*x  
print(d)    
        
