def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    y = float(input("Enter second number: "))
    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if op not in ops:
        print("Invalid operation")
    else:
        try:
            print("Result:", ops[op](x, y))
        except ValueError as e:
            print("Error:", e)