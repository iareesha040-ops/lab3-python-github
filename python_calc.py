def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: cannot divide by zero")
    else:
        print("Result:", a / b)

def even_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

def percentage(a, b):
    if b == 0:
        print("Error: cannot divide by zero")
    else:
        print("Percentage:", (a / b) * 100, "%")

while True:
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))
    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))
    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))
    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        divide(a, b)
    elif choice == "5":
        n = int(input("Enter a number: "))
        even_odd(n)
    elif choice == "6":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        percentage(a, b)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")
        
