n=int(input("Enter the number: "))

total=0
pattern=""
for i in range(1,n+1):
    total+=i
    if i==1:
        pattern=1
    else:
        pattern=str(pattern) + " + " + str(i)
    print(f"{pattern} = {total}")
'''    
n = int(input("Enter a number: "))
history = []
total = 0

for i in range(1, n + 1):
    total += i
    history.append(str(i)) # Store the number as a string
    
    # "Join" all numbers in the list with a " + " between them
    print(f"{' + '.join(history)} = {total}")
'''    
