# prompt user for pattern size
size = int(input("Enter the size of the pattern: "))
#Ensure the inpit is a postive integer
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))
#Draw the pattern using nested loops
row = 0
while row < size: 
    for col in range(size):
# print astericks for each column in the row
        print("*", end= " ")
    print ()
# Move to the next row after completing the current row 
    row += 1
