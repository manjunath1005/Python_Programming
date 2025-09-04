def fun(n):
    for i in range(n):
        for j in range(n):
            if(i==j):
                print('$',end="")
            else:
                print("*",end="")
        print()
fun(int(input("Enter Number:")))