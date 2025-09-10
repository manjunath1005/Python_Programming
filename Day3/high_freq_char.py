def fun(st):
    li=[]
    c=0
    ch=""
    for i in st:
        if i not in li:
            li.append(i)
            if st.count(i) > c:
                c = st.count(i)
                ch=i
    print("Highest Frequency character",ch)

st=input("Enter a String:")
fun(st)