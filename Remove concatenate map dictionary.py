#Remove a Key from a Dictionary
d={'a': 1, 'c': 3, 'b': 2, 'd': 4}
key=input("Enter the key to be removed:")
del d[key] #or d.pop(key)
print(d)

#Concatenate Two Dictionaries
d1={'a': 1, 'c': 3, 'b': 2, 'd': 4}
d2={'e': 5}
d1.update(d2)
print(d1)

#Map Two Lists into a Dictionary
d={}
key=[]
value=[]
n=int(input("Enter the number of dict:"))
for i in range(n):
    k=input(f"Enter the key {i+1}:")
    key.append(k)    
for i in range(n):    
    val=input(f"Enter the value {i+1}:")
    if val.isdigit():
        v=int(val)
    else:
        v=val
    value.append(v)   
d=dict(zip(key,value))
print(d)    
