
import math
num=int(input("Enter the num: "))
prime=True
if(num<2):
    prime=False
else:    
 for i in range(2,int(math.sqrt(num)+1)):
   
    if(num%i==0):
        prime=False
        break
    
if prime:
    print(num,"is prime")
else:
    print(num,"is not prime")