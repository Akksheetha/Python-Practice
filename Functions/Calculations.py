def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def callback(operation, operand1, operand2):
    result = operation(operand1, operand2)
    return result
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print("Add:", callback(add, a, b))
print("Subtract:", callback(subtract, a, b))
print("Multiply:", callback(multiply, a, b))