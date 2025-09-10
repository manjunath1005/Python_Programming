def fun(st):
    c=0
    for i in st.split():
        c+=1
    print("No.of words:",c)

s=input("Enter the string:")
fun(s) 