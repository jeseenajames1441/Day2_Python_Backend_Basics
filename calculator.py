def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("===== SIMPLE CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")


if choice not in ["1", "2", "3", "4"]:
    print("Invalid option  Please choose between 1 to 4")

else:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))

    elif choice == "2":
        print("Result:", sub(a, b))

    elif choice == "3":
        print("Result:", mul(a, b))

    elif choice == "4":
        print("Result:", div(a, b))