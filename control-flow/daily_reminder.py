Task = input("Enter your task: ")
Time_bound = input(" Is it time-bound? (yes or no): ")
Priority = input("Priority (high, medium, low): ")
if Time_bound == "yes":
 match Priority:
    case "high":
     print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
    case "medium":
     print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
    case "low":
     print(f"Reminder: {Task} is a {Priority} priority task that requires attention today!")
if Time_bound == "no":
 match Priority:
    case "low":
     print (f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
        print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")