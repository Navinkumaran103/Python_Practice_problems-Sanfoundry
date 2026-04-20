#Check substring [can be done with in or find()]
string=input("Enter the strings:")
substring=input("Enter the substring:")

if substring in string:
    print("Substring in string!")
else:
    print("Substring not found in string!")
