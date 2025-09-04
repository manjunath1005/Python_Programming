def palindrome(n):
    for i in range(n):
        i=str(i)
        if i==i[-1::-1]:
            print(i,end=" ")
palindrome(int(input("Enter Number:")))
        