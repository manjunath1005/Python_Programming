# Write a function(preLetterCase) that accepts two parameters ( a string ,and a letter). The function must return the string with all characters before the first instance of the letter converted to lowercase and all other characters converted to uppercase. Hence, if the specified letter is the first character of the string then the entire string will be converted to uppercase. The new string should be returned by the function.
def preLetterCase(s,le):
    i=s.index(le)
    return s[:i].lower()+s[i:].upper()

s,le=input("Enter the String and a letter:").split()
print(preLetterCase(s,le))