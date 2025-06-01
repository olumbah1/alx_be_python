task = input("Enter a task description: ")
priority = input("Enter task's priority(high, medium, low: ")
time_bound = input("Enter, if task is time-bound? yes or no: ")
if time_bound == "yes":
 match priority:
    case "high":
     print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case "medium":
     print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case "low":
     print(f"Reminder: {task} is a {priority} priority task that requires attention today!")
if time_bound == "no":
 match priority:
    case "low":
     print (f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")