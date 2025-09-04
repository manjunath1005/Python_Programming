def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
    
def strong(n):
    for i in range(1,n):
        t=i
        s=0
        while t>0:
            s=s+fact(t%10)
            t=t//10
        if s==i:
            print(i)

strong(int(input("Enter a number:")))