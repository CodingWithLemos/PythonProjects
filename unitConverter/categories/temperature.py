# Temperature Module with Various Unit Conversions

# main module
def main(conversion):
    #  function body
    def celsiusToFahrenheit(T):
        fahrenheit = 1.8*T+32
        return fahrenheit

    def celsiusToKelvin(T):
        kelvin = T + 273.15
        return kelvin

    def fahrenheitToCelsius(T):
        celsius = ( T - 32 ) / 1.8
        return celsius

    def fahrenheitToKelvin(T):
        kelvin = (T + 459.67) / 1.8
        return kelvin

    def kelvinToCelsius(T):
        celsius = T - 273.15
        return celsius

    def kelvinToFahrenheit(T):
        fahrenheit = (T * 1.8) - 459.67
        return fahrenheit

    # matching each function to conversion types input by user
    match conversion:
        case 'celsius > fahrenheit':
            print(f'Temperature in Fahrenheit: {celsiusToFahrenheit(T):.2f}')
        case 'celsius > kelvin':
            print(f'Temperature in Kelvin: {celsiusToKelvin(T):.2f}')
        case 'fahrenheit > celsius':
            print(f'Temperature in Celsius: {fahrenheitToCelsius(T):.2f}')
        case 'fahrenheit > kelvin':
            print(f'Temperature in Kelvin: {fahrenheitToKelvin(T):.2f}')
        case 'kelvin > celsius':
            print(f'Temperature in Celsius: {kelvinToCelsius(T):.2f}')
        case 'kelvin > fahrenheit':
            print(f'Temperature in Fahrenheit: {kelvinToFahrenheit(T):.2f}')
        case _:
            print('Invalid conversion!')

if __name__ == "__main__":
    import sys
    T = int(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)