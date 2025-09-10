def fun(li):
    vis=[]
    for i in li:
        if i not in vis:
            vis.append(i)
    return vis

li=input().split()
print(fun(list(li)))