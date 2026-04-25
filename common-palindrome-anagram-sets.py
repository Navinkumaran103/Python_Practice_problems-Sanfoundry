#Find common characters in two strings
first=input("Enter the first string:")
second=input("Enter the second string:")

common=set(first) & set(second)
for i in common:
    print(i)

      
#Palindrome
string=input("Enter the string:")
compare=string[::-1]
print(f"string:{string} and compare:{compare}")
if(compare==string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

      
#Anagram
first=input("Enter the first string:")
second=input("Enter the second string:")

if sorted(first) == sorted(second):
    print("Anagram")
else:
    print("Not Anagram")      

#Count vowels using sets
string=input("Enter the string:")
vowels=set("aeiou")
count=0
for i in string:
    if i in vowels:
        count+=1
print(count)        
