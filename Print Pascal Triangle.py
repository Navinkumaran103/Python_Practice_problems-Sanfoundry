n=int(input("Enter the rows:"))
pascal=[]
for i in range(n):
    row=[]
    for j in range(i+1):
        if(j==0 or j==i):
            row.append(1)
        else:
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
    pascal.append(row)
    
    space=" " * (n-i)
    rowstr=" ".join(map(str,row))
    print(space+rowstr)
        
