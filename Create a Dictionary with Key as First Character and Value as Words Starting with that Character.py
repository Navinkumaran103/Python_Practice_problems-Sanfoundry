#Create a Dictionary with Key as First Character and Value as Words Starting with that Character
string=input("Enter the string:")
w=string.split(" ")
d={}
for word in w:
    key=word[0].lower()
    if key not in d.keys():
        d[key]=[word]
    else:
        if word not in d[key]: #removes repeated word
            d[key].append(word)
print(d)            
for k,v in d.items():
    print(k,':',v)
'''
test_string=input("Enter string:")
l=test_string.split()
d={}
for word in l:
    key=word[0].lower()
    if(key not in d.keys()):
        d[key]=[]
        d[key].append(word)
    else:
        if(word not in d[key]):
          d[key].append(word)
for k,v in d.items():
        print(k,":",v)
'''       
