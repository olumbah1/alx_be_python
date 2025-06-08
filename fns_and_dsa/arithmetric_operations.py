  
def perform_operation(num1: float, num2: float, operation: str):
    operations = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }
    if operation in operations:
        return operations[operation](num1, num2)
    else:
        return "Error: Invalid operation"