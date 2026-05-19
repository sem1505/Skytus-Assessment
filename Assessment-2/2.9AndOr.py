x = int(input("Enter a first number 0 or 1:"))
y = int(input("Enter a Second number 0 or 1:"))

print("And Operator :")
if x == 1 and y == 1:
    print("1")
    
elif x == 1 and y == 0:
    print("0")
    
elif x == 0 and y == 1:
    print("0")
    
else:
    print("0")
    
print("Or Operator :")
if x == 1 or y == 1:
    print("1")

elif x == 1 or y == 0:
    print("1")
    
elif x == 0 or y == 1:
    print("1")
    
else:
    print("0")
    