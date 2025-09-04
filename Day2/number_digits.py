def fun(n):
    i=0
    while n>0:
        n//=10
        i+=1
    return i
n=int(input("Enter Number:"))
print(fun(n))