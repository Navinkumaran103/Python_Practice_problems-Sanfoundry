n=int(input("Enter the number: "))
dig=n
temp=0
while(n>0):
    num=n%10
    n=n//10
    temp=(temp*10)+num
if(dig==temp):
    print(dig, "is Palindrome")
else:
    print(dig, "is not Palindrome")