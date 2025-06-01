number = int(input("Enter a number to see its multiplication table: "))
print(number)
for Y in range (1, 11):
    Z = number * Y
    print(f" {number} * {Y} = {Z}")