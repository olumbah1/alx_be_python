def checker(number):
    return number % 2 == 0
user_input = int(input( "Enter a number: "))
if checker(user_input):
    print(f'The number is even.')
else :
     print(f'The number is odd. ')