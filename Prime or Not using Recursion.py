def prime(n,div=None):
    
    if n<2:
        print("1 is not prime or composite")
        return False
    
    if div is None:div=n-1
    
    if div<2:
        print("It is prime")
        return True
    
    if n%div==0:
        print("It is not prime")
        return False
    
    return prime(n,div-1)

    
num=int(input("Enter the num: "))
prime(num)