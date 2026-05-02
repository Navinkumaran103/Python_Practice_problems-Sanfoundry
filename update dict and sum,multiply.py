#Add a Key-Value Pair to the Dictionary
key=input("Enter the key:")
value=input("Enter the value:")
d={}
d.update({key:value})
print(d)


#Sum of All the Items in a Dictionary
n=int(input("Enter the number of dict to be entered:"))
d={}
while n>0:
    key = input("Enter the key: ")
    val = input("Enter the value: ")
    if val.isdigit():
        value = int(val)
    else:
        value = val       
    d.update({key:value})
    n=n-1
print(f"sum: {sum(d.values())}")


#Multiply All the Items in a Dictionary
n=int(input("Enter the number of dict to be entered:"))
d={}
while n>0:
    key = input("Enter the key: ")
    val = input("Enter the value: ")
    if val.isdigit():
        value = int(val)
    else:
        value = val       
    d.update({key:value})
    n=n-1
total=1
for i in d:
    total=total*d[i]
print(f"Multiply: {total}")
