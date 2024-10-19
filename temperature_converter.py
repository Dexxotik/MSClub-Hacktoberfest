# temperature_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)

def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)

def main():
    print("Temperature Converter")
    print("Select conversion type:")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("5: Fahrenheit to Kelvin")
    print("6: Kelvin to Fahrenheit")

    choice = input("Enter the number of your choice: ")

    temp = float(input("Enter temperature: "))

    if choice == '1':
        print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    elif choice == '2':
        print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    elif choice == '3':
        print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
    elif choice == '4':
        print(f"{temp}K is {kelvin_to_celsius(temp)}°C")
    elif choice == '5':
        print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
    elif choice == '6':
        print(f"{temp}K is {kelvin_to_fahrenheit(temp)}°F")
    else:
        print("Invalid choice. Please select a valid conversion type.")

if __name__ == "__main__":
    main()
