def bill(n):
    if n<=50:
        return n*3.80
    elif n<=100:
        return 50*3.80 + (n-50)*4.2
    elif n<=200:
        return 50*3.80 + 50*4.2 + (n-100)*5.1
    elif n<=300:
        return 50*3.80 + 50*4.2 + 100*5.1 + (n-200)*6.5
    else:
        return 50*3.80 + 50*4.2 + 100*5.1 + 100*6.5 + (n-300)*7.8
    
n=int(input("Enter the number of units consumed:"))
print(bill(n))