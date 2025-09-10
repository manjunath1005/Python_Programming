def fun(li):
    li.sort()
    return li[-2]
while True:
    c=int(input("Enter 1 for adding input or 0 for Exit:"))
    if c==1:
        i=list(map(int,input().split()))
        print(fun(i))
    else:
        break