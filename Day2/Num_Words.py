def fun(n):
    s=str(n)
    i=0
    while i<len(s):
        if s[i]=='1':
            print("One",end=" ")
        elif s[i]=='2':
            print("Two",end=" ")
        elif s[i]=='3':
            print("Three",end=" ")
        elif s[i]=='4':
            print("Four",end=" ")
        elif s[i]=='5':
            print("Five",end=" ")
        elif s[i]=='6':
            print("Six",end=" ")
        elif s[i]=='7':
            print("Seven",end=" ")
        elif s[i]=='8':
            print("Eight",end=" ")
        elif s[i]=='9':
            print("nine",end=" ")
        elif s[i]=='0':
            print("Zero",end=" ")
        i+=1
fun(input("Enter a Number:"))