name = input("What is your name? ")
age = int(input("How old are you? "))

next_age = age + 1

print("Hello,", name)
print("Next year you wil be", next_age)


if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager")
else:
    print("You are an adult.")