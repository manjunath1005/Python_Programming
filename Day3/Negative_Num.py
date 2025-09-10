def fun(li):
    return [i for i in li if i<0]
while True:
    c=int(input("Enter 1 for adding input or 0 for Exit:"))
    if c==1:
        i=list(map(int,input().split()))
        print(fun(i))
    else:
        break