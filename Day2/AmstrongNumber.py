def Amstrong(n):
    t=n
    s=0
    while n>0:
        s=s+(n%10)**3
        n//=10
    if s==t:
        print("Amstrong Number")
    else:
        print("Not an Amstrong Number")
Amstrong(int(input("Enter a Number:")))