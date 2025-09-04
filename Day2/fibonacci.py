def fib(n):
    n1=0
    n2=1
    for i in range(n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")
fib(int(input("Enter a Number:")))