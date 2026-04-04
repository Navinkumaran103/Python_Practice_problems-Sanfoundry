def poweroftwo(n):
    if n<=0:
        return False
    if n>=1:
        return n & n-1 == 0
      

n=int(input("ENter the number:"))
if poweroftwo(n):
    print(n,"is power of two")
else:
    print(n,"is not power of two")


'''
4=100    8=1000  16=10000
3=011    7=0111  15=01111 
4&3==0   8&7==0  16&15==0
'''
