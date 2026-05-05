#Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
num1=int(input("Enter the start num:"))
num2=int(input("Enter the end num:"))
templist=[]
for i in range(num1,num2+1):
    element=(i,i*i)#create tuple element(number,square)
    templist.append(element)
#a=[(i,i*i) for i in range(num1,num2+1)]    print(a)
print(tuple(templist))


#Remove All Tuples in a List Outside the Given Range
y=[('a','12CS039'),('b','12CS320'),('c','12CS055'),('d','12CS100')]
result=[]
num1=int(input("Enter the start num:"))
num2=int(input("Enter the end num:"))
for label,idstr in y:
    idstr=int(idstr[4:])
    if idstr<num1 or idstr>num2:
        result.append((label,idstr))
print(tuple(result))   

#Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple
def last(n):
    return n[-1]
user_input=input("Enter the list of tuples:")
num=eval(user_input) #Passing __import__('os').system('rm -rf /a-path-you-really-care-about') into ast.literal_eval() will raise an error, 
                     #but eval() will happily delete your files.
end=sorted(num, key=last)
print(end)



