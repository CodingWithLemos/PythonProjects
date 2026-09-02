# Mass Module with Various Unit Conversions

# function definition
def massConverter(
        amt,
        input_unit,
        output_unit):
    
    """ prompt user to input mass and conversion type, 
    then convert mass to desired unit """

    match input_unit, output_unit:
        case 'kilograms', 'pounds':
            result = amt * 2.20462
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'pounds', 'kilograms':
            result = amt / 2.20462
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'kilograms', 'ounces':
            result = amt * 35.274
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'ounces', 'kilograms':
            result = amt / 35.274
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'pounds', 'ounces':
            result = amt * 16
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'ounces', 'pounds':
            result = amt / 16
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')
        
        case _:
            print('Invalid conversion!')

# main module
if __name__ == "__main__":
    import sys
    amt = float(sys.argv[1])
    input_unit = sys.argv[2]
    output_unit = sys.argv[3]

    massConverter(amt, input_unit, output_unit)

