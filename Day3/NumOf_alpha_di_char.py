def fun(st):
    a=d=c=0
    for i in st:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            d+=1
        else:
            c+=1
    print("No.of Alphabets:",a,"\nNo.of Digits:",d,"\nNo.of Special Characters:",c)

s=input("Enter the string:")
fun(s)