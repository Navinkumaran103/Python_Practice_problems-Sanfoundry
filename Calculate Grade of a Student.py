n=int(input("Enter the number of subjects: "))
marks=[]
for i in range(1,n+1):
    print("enter the sub",i, " mark")
    x=int(input())
    marks.append(x)
avg=(sum(marks))/n    
print("Average of",n,"subjects is", avg)
if avg >= 90:
    print("Grade: A")
elif avg >= 80 and avg < 90:
    print("Grade: B")
elif avg >= 70 and avg < 80:
    print("Grade: C")
elif avg >= 60 and avg < 70:
    print("Grade: D")
else:
    print("Grade: F")
    