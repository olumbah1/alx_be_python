def perform_operation(num1: float, num2: float, operation: str):
    operations = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: a / b if b != 0 else float('inf')
    }
    if operation in operations:
     return operation[operation](num1, num2)
    else:
     raise ValueError(f"Invalid operation: {operation}")
   