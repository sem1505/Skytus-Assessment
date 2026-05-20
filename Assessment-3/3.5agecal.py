import datetime

birth = int(input("Enter your birth year: "))

current = datetime.datetime.today().year

age = current - int(birth)

print("Your age is: ", age , " years old.")