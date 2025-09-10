def fun(li):
    vis=[]
    for i in li:
        if i not in vis:
            c=0
            for j in li:
                if i==j:
                    c+=1
            if c==1:
                vis.append(i)
    print(vis)
i=list(map(int,input().split()))
fun(i)