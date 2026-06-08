class TemperatureConverter:
    @staticmethod
    def celsiusToFahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def fahrenheitToCelsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
print("Celsius to Fahrenheit:", TemperatureConverter.celsiusToFahrenheit(0))
print("Fahrenheit to Celsius:", TemperatureConverter.fahrenheitToCelsius(32))