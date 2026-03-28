date_input = input("Enter the date(dd/mm/yyyy): ")

try:
    dd, mm, yyyy = map(int, date_input.split('/'))

    if yyyy > 4000:
        print(f"--- Warning: Year {yyyy} is in the distant future. ---")

    if mm in [1, 3, 5, 7, 8, 10, 12]:
        maxdd = 31
    elif mm in [4, 6, 9, 11]:
        maxdd = 30
    elif (yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0):
        maxdd = 29
    else:
        maxdd = 28

    if mm < 1 or mm > 12:
        print("Error: Month must be between 1 and 12.")
    elif dd < 1 or dd > maxdd:
        print(f"Error: Day {dd} is invalid for month {mm} in year {yyyy}.")
    else:
        if dd == maxdd:
            dd = 1
            if mm == 12:
                mm = 1
                yyyy += 1
            else:
                mm += 1
        else:
            dd += 1

        print(f"The incremented date is: {dd:02d}/{mm:02d}/{yyyy}")

except ValueError:
    print("Error: Please use the format dd/mm/yyyy (numbers only).")
    
'''
date=input("Enter the date(dd/mm/yyyy):")

dd,mm,yyyy=map(int, date.split('/'))

if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    maxdd=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    maxdd=30
elif(yyyy%4==0 and yyyy%100!=0 or yyyy%400==0):
    maxdd=29
else:
    maxdd=28

if(dd<1 or dd>maxdd):
    print("Date is invalid")
elif(mm<1 or mm>12):
    print("Date is invalid")
elif(dd==31 and mm==12):
    dd=1
    mm=1
    yyyy=yyyy+1
    print("The incremented date is: ",dd,mm,yyyy)
elif(dd==maxdd and mm!=12):
    dd=1
    mm=mm+1
    print("The incremented date is: ",dd,mm,yyyy)
else:
    dd=dd+1
    print("The incremented date is: ",dd,mm,yyyy)
'''    
    
    