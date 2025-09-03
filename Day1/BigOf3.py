def fun(a,b,c):
    if a>b:
        if a>c:
            print(a,"is Greatest")
        else:
            print(c,"is Greatest")
    elif b>a:
        if b>c:
            print(b,"is Greatest")
        else:
            print(c,"is Greatest")
    else:
        print(c,"is Greatest")
n=list(map(int,input("Enter 3 Numbers").split()))
fun(n[0],n[1],n[2])