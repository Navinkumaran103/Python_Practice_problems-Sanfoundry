
def func(num):
    if(num<=0):
        return num
    else:
        return num%10 + func(num//10)

n=int(input("Enter the number: "))

dig=func(n)
print(dig)

'''
l=[]
def sum_digits(b):
    if(b==0):
        return l
    dig=b%10
    l.append(dig)
    sum_digits(b//10)
n=int(input("Enter a number: "))
sum_digits(n)
print(sum(l))
'''