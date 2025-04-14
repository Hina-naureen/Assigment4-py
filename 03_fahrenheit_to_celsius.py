def fahrenheit_to_celsius():
    try:
        # User se input lena
        degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        # Conversion formula
        degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

        # Output with proper formatting
        print(f"\nTemperature: {degrees_fahrenheit:.1f}F = {degrees_celsius:.15f}C")

    except ValueError:
        print("Invalid input! Please enter a valid number (e.g., 76 or 76.5).")

# Run the function
if __name__ == "__main__":
    fahrenheit_to_celsius()
