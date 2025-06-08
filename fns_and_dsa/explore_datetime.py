from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now 
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time:", formatted)
    

def  calculate_future_date():
     try:
         number_of_days = int(input("Enter a number of days: "))
         current_date = datetime.now()
         future_date = current_date + timedelta(days=number_of_days)
         formatted = future_date.strftime("%Y-%m-%d")
         print(f"Future Date:", formatted)
     except ValueError:
        print("Enter the number of days to add to the current date:")