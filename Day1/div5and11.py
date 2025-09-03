def fun(n):
    if n%5==0 and n%11==0:
        print("Number is divisible by 5 and 11")
    else:
        print("Number is not divisible by 5 and 11")
n=int(input("Enter a number:"))
fun(n)