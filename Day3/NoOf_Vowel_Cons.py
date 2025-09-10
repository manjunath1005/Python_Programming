def fun(st):
    v=c=0
    for i in st:
        if i in 'aeiouAEIOU':
            v+=1
        elif i.isalpha():
            c+=1
    print("No.of Vowels:",v,"\nNo.of Consonants:",c)

s=input("Enter the string:")
fun(s)