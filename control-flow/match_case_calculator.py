num1 = int(input("Enter a number:, "))
num2= int(input("Enter a number:, "))
type_of_operation = input("Choose the operation (+, -, *, /):, ")
match type_of_operation:
    case "+":
     print(f"{num1} + {num2} = {num1 + num2}")
match type_of_operation:
    case "-":
     print(f"{num1} - {num2} = {num1 - num2}")
match type_of_operation:
    case "*":
     print(f"{num1} * {num2} = {num1 * num2}")
match type_of_operation:
    case "/":
     print(f"{num1} / {num2} = {num1 / num2}")
     if num2 != 0:
      print(f"{num1} / {num2} = {num1 / num2}")
     else:
         print("Error: Division by zero.")
    case _:
        print("Invalid operation.")
    
 