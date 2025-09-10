def freq(li):
    vis=[]
    for i in range(len(li)):
        if li[i] not in vis:
            c=0
            for j in range(len(li)):
                if li[i]==li[j]:
                    c+=1
            print(f"{li[i]}->{c}")
            vis.append(li[i])


i=list(map(int,input().split()))
freq(i)