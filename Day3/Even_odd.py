e=[]
o=[]
def fun(li):
    for i in li:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
while True:
    c=int(input("Enter 1 for adding input or 0 for Exit:"))
    if c==1:
        i=list(map(int,input().split()))
        fun(i)
        print("Even:",e,"\nOdd:",o)
    else:
        break