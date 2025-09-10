def len(st):
    c=0
    for i in st:
        c+=1
    print("Length of String:",c)

def compare(s1,s2):
    if l1==l2:
        if(s1==s2):
            print("Both Strings are Equal")
        else:
            print("Both strings are not Equal")
    else:
        print("Both strings are not Equal")

    print("Concatinated String:",s1+s2)

    
s1=input("Enter a String:")
l1=len(s1)
s2=input("Enter another String:")
l2=len(s2)
compare(s1,s2)
