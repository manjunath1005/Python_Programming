def fun(n):
    i=0
    l=n%10
    while n>9:
        f=n//10
        n//=10
    return l+f
n=int(input("Enter Number:"))
print("Sum of First and Last Term is",fun(n))