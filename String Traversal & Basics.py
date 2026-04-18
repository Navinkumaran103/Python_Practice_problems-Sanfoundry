"""
#Count vowels
string=input("Enter the words:")
vowels=0

for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels+=1
print(vowels) 
"""
"""
#Count uppercase/lowercase
string=input("Enter the words:")
lower=0
upper=0
for i in string:
    if(i.islower()):
        lower+=1
    elif(i.isupper()):
        upper+=1
print("lower count:",lower)
print("upper count:",upper) 
"""

"""
#Count digits,characters and letters
string=input("Enter the input:")
digits=0
letters=0
characters=0
for i in string:
    if(i.isdigit()):
        digits+=1
    elif(i.isascii()):
        letters+=1
    characters+=1    
print("digits count:",digits)
print("letters count:",letters) 
print("characters count:",characters) 
"""
