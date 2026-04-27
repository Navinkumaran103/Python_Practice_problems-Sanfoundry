#Check if a Key Exists in a Dictionary or Not

key=input("Enter Key to check:")
dictionary={"A":1,"B":2,"C":3}
if key in dictionary:
    print(dictionary[key])
else:
    print("No key found")
