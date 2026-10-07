number = int(input("What number would you like a multiplication table for?"))

starter = 1

for starter in range(1,11):
    total = number * starter
    print(number, "x", starter, "=", total)