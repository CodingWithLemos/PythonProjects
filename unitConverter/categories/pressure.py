# Pressure Module with Various Unit Conversions

# function definition
def pressureConverter(
        amt,
        input_unit,
        output_unit):
    
    """ prompt user to input pressure and conversion type, 
    then convert pressure to desired unit """

    match input_unit, output_unit:
        case 'hectopascal', 'bar':
            result = amt / 1000
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'bar', 'hectopascal':
            result = amt * 1000
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'hectopascal', 'inches of mercury':
            result = amt * 33.86
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'inches of mercury', 'hectopascal':
            result = amt / 33.86
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'bar', 'inches of mercury':
            result = amt * 29.53
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'inches of mercury', 'bar':
            result = amt / 29.53
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')
        
        case _:
            print('Invalid conversion!')

# main module
if __name__ == "__main__":
    import sys
    amt = float(sys.argv[1])
    input_unit = sys.argv[2]
    output_unit = sys.argv[3]

    pressureConverter(amt, input_unit, output_unit)