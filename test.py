print("password checker")
import time
print("A good password should have an uppercase letter, a lowercase letter, a symbol, and a number. \nIt should also be longer then 6 characters.")

p = input(("Enter the password you want to check: "))

upper_case = 0
lower_case = 0
number = 0
symbol = 0

for i in p:
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1
    elif i.isdigit():
        number += 1
    else:
        symbol += 1

if len (p) <= 6:
    print("This is a weak password. Try adding more then 6 characters.")
elif upper_case > 0 and lower_case > 0 and number > 0 and symbol > 0:
    print ("This password is good.")
else:
    print ("This password is weak.")

input("Press enter to exit!")
