def del_ele(li,i):
    li=li[:i]+li[i+1:]
    return li


i=list(map(int,input().split()))
index=int(input("Enter the index to be deleted:"))
print(del_ele(i,index))
