# Temperature Module with Various Unit Conversions

# function definition
def temperatureConverter(
        amt,
        input_unit,
        output_unit):
    
    """ prompt user to input temperature and conversion type, 
    then convert temperature to desired unit """

    match input_unit, output_unit:
        case 'celsius', 'fahrenheit':
            result = 1.8 * amt + 32
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'fahrenheit', 'celsius':
            result = (amt - 32) / 1.8
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'celsius', 'kelvin':
            result = amt + 273.15
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'kelvin', 'celsius':
            result = amt - 273.15
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'fahrenheit', 'kelvin':
            result = (amt - 32) / 1.8 + 273.15
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'kelvin', 'fahrenheit':
            result = (amt - 273.15) * 1.8 + 32
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')
        
        case _:
            print('Invalid conversion!')

# main module
if __name__ == "__main__":
    import sys
    amt = float(sys.argv[1])
    input_unit = sys.argv[2]
    output_unit = sys.argv[3]

    temperatureConverter(amt, input_unit, output_unit)