def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

conversion_functions = {
    "1": ("To Convert Celsius to Fahrenheit", celsius_to_fahrenheit, "°F"),
    "2": ("To Convert Fahrenheit to Celsius", fahrenheit_to_celsius, "°C"),
    "3": ("To Convert Celsius to Kelvin", celsius_to_kelvin, "K"),
    "4": ("To Convert Kelvin to Celsius", kelvin_to_celsius, "°C")
}

while True:
    print("\n***TEMPERATURE CONVERSION***")
    for key, (desc, _, _) in conversion_functions.items():
        print(f"{key}. {desc}")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting the converter.")
        break

    if choice in conversion_functions:
        try:
            value = float(input("Enter the temperature value: "))
            desc, func, unit = conversion_functions[choice]
            result = func(value)
            print(f"{desc}: {value} → {result:.2f} {unit}")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Invalid option!!!Please choose between 1 and 5.")
