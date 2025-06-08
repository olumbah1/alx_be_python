FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")

# Main program
try:
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        convert_to_celsius(temp)
    elif unit == "C":
        convert_to_fahrenheit(temp)
    else:
        print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid temperature entered. Please enter a numeric value.")
