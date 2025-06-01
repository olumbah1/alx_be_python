print("Input two numbers at a time")
num1 = int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
type_of_operation = input("Choose the operation (+, -, *, /): ")
match type_of_operation:
    case "+":
     result = num1 + num2
     print(f"The result is {result}")
    case "-":
       result = num1 - num2
       print(f"The result is {result}")
    case "*":
       result = num1 * num2
       print(f"The result is {result}")
    case "/":
       result = num1 / num2
       print(f"The result is {result}")
       if num2 != 0:
        result = num1 / num2
        print(f"The result is {result}")
       else:
           print("Error: Cannot divide by zero.")
    case _:
        print("Invalid operation.")

    
 