s=[]
def fun(li):

    s.append(li)
    
while True:
    c=int(input())
    if c==1:
        i=int(input())
        fun(i)
    else:
        break
print(s)