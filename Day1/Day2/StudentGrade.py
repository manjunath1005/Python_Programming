def grade(n):
    if n>80:
        return "Distinction"
    elif n>70:
        return "A"
    elif n>50:
        return "B"
    elif n>40:
        return "C"
    else:
        return "Fail"
    
n=int(input("Enter the marks: "))
print(grade(n))