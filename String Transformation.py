#Reverse a String with slicing
string=input("Enter the string:")
print(string[::-1])

#Reverse a String with concatanation 
string=input("Enter the string:")
rev_str=""
for i in string:
    rev_str=i+rev_str
print(rev_str)  

#Remove nth index character
string=input("Enter the string:")
n=int(input("Enter the index to be removed:"))
print(string[:n] + string[n+1:])

#Replace characters in string
string=input("Enter the string:")
r=input("Enter the character to be replaced:")
rep=input("Enter the character to be replaced with:")
for i in string:
    if ((i==r) or (i==r.casefold())):
        i=rep
    print(i,end="")    
