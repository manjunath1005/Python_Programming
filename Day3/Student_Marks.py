def fun(tu):
    for i in tu:
        if i[2]>75:
            print(i[:2])

li=[]
n=int(input("Enter Number of Students:"))
for i in range(n):
    id=int(input("Enter the ID:"))
    name=input("Enter the name:")
    marks=int(input("Enter the marks:"))
    li.append((id,name,marks))
t=tuple(li)
fun(t)