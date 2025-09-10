def fun(st):
    li=[]
    c=""
    for i in st:
        if i not in li:
            li.append(i)
            c+=i+str(st.count(i))
    print(c)

st=input("Enter a String:")
fun(st)