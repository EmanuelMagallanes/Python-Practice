def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return("Cannot divide by zero")
    else:
        return a / b

a = int(input("First number:"))
b = int(input("Second number:"))

operation = input("Operation:")

if operation == "+":
    Result = add(a, b)
elif operation == "-":
    Result = subtract(a, b)
elif operation == "*":
    Result = multiply(a, b)
elif operation == "/":
    Result = divide(a, b)
else:
    Result = "Invalid operation"

print("Result:", Result)



