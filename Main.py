from FinonacciConversion import FibonacciConversion
from FahrenheitToCelsius import FahrenheitToCelsius


def main():
    print("What would you like to do?")
    userInput = input("Press 'F' for Celsius conversion\n"
                      "Press 'N' for Fibonacci conversion\n"
                      "Press 'Q' to quit\n")

    if userInput == 'F':
        fahrenheit = input("Enter the temperature in degrees Fahrenheit")
        fahrenheit = float(fahrenheit)
        print(FahrenheitToCelsius(fahrenheit))

    elif userInput == 'N':
        fibonacciNumber = input("Enter the number you'd like to convert")
        fibonacciNumber = int(fibonacciNumber)
        print(FibonacciConversion(fibonacciNumber))

    elif userInput == 'Q':
        print("Goodbye")

    else:
        print("Invalid input")

main()
