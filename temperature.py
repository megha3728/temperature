import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

if __name__ == "__main__":
    print("Convert Celsius to Fahrenheit")

    
    if len(sys.argv) != 2:
        print("Error: Please provide temperature in Celsius as argument")
        print("Usage: python temperature.py <celsius>")
        sys.exit(1)

    try:
        celsius = float(sys.argv[1])
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

    except ValueError:
        print("Error: Celsius value must be a number")
        sys.exit(1)