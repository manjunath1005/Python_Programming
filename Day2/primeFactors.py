def isprime(n):
    if n<=1:
        return False
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return True
    else:
        return False
def prime(n):
    for i in range(1,n):
        if(n%i==0):
            if(isprime(i)):
                print(i)
prime(int(input("Enter a Number:")))