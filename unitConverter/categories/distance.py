# Distance Module with Various Unit Conversions

# function definition
def distanceConverter(
        amt,
        input_unit,
        output_unit):
    
    """ prompt user to input distance and conversion type, 
    then convert distance to desired unit """

    match input_unit, output_unit:
        case 'kilometers', 'miles':
            result = amt / 1.60934
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'miles', 'kilometers':
            result = amt * 1.60934
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'kilometers', 'nautical miles':
            result = amt + 273.15
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'nautical miles', 'kilometers':
            result = amt * 1.852
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'miles', 'nautical miles':
            result = (amt - 32) / 1.8 + 273.15
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'nautical miles', 'miles':
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

    distanceConverter(amt, input_unit, output_unit)