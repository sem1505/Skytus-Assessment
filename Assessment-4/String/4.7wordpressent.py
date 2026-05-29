a = str(input("Enter a string: "))
b = str(input("Enter a word to find: "))

if b.lower() in a.lower():
    print("The word is present in the string.")
else:
    print("The word is not present in the string.")