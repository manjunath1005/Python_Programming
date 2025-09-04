def week(n):
    if n==1:
        return "Monday"
    elif n==2:
        return "Tuesday"
    elif n==3:
        return "Wednesday"
    elif n==4:
        return "Thursday"
    elif n==5:
        return "Friday"
    elif n==6:
        return "Saturday"
    elif n==7:
        return "Sunday"
    else:
        return "Invalid input"

n=int(input("Enter a number (1-7): "))
print(week(n))