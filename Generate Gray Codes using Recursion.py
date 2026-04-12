def gray(n):
    if(n==1):
        return ["0","1"]
        
    prev_list=gray(n-1)
    rev_list=prev_list[::-1]
    res1 = ["0" + x for x in prev_list]
    res2 = ["1" + x for x in rev_list]
    return res1+res2
n=int(input("Enter the range: "))
print(gray(n))

"""
to generate gray code --> reflect & resolve
i.e. solve(n-1) and reflect-reverse it
prefix "0" to original list
prefix "1" to reverse list 
"""
