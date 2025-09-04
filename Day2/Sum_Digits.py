def fun(n):
    i=0
    sum=0
    s=str(n)
    while i <=len(s):
        sum+=n%10
        n//=10
        i+=1
    return sum
n=int(input("Enter a Number:"))
print(fun(n))