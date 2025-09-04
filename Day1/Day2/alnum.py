def fun(s):
    if s.isalpha():
        print("Alphabet")
    elif s.isdigit():
        print("Digit")
    else:
        print("Special Character")
        
s=input("Enter a character:")
fun(s)