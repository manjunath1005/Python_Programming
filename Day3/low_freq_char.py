def fun(st):
    li=[]
    ch=""
    c=10**100
    for i in st:
        if i not in li:
            li.append(i)
            if st.count(i) < c:
                c = st.count(i)
                ch=i
    print("Lowest Frequency character",ch)

st=input("Enter a String:")
fun(st)