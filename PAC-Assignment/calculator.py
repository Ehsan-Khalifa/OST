def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("16 + 4 =", add(16, 4))
    print("16 - 4 =", subtract(16, 4))
    print("16 * 4 =", multiply(16, 4))
    print("16 / 4 =", divide(16, 4))
