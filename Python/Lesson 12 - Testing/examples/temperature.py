# temperature.py
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not possible")
    return (celsius * 9 / 5) + 32
