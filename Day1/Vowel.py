vowel=['a','e','i','o','u']
def fun(n):
    if n.lower() in vowel:
        print("Vowel")
    else:
        print("Consonant")
n=input("Enter an Alphabet:")
fun(n)