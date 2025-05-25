Monthly_Income = input("Enter your monthly income:")
Monthly_Expenses = input("Enter your total monthly expenses:")
Monthly_Savings = Monthly_Income - Monthly_Expenses
Annual_Interest_rate = 0.05
print(Monthly_Income)
print(Monthly_Expenses)
print(Monthly_Savings)
print(f"Projected Savings = {Monthly_Savings * 12 + Monthly_Savings * 12 * 0.05}")