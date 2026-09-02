# Velocity Module with Various Unit Conversions

# function definition
def velocityConverter(
        amt,
        input_unit,
        output_unit):
    
    """ prompt user to input fuel economy and conversion type, 
    then convert fuel economy to desired unit """

    match input_unit, output_unit:
        case 'kilometer per hour', 'miles per hour':
            result = amt / 1.60934
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'miles per hour', 'kilometer per hour':
            result = amt * 1.60934
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'kilometer per hour', 'knots':
            result = amt / 1.852
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'knots', 'kilometer per hour':
            result = amt * 1.852
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'miles per hour', 'knots':
            result = amt / 1.15078
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'knots', 'miles per hour':
            result = amt * 1.15078
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')
        
        case _:
            print('Invalid conversion!')


# main module
if __name__ == "__main__":
    import sys
    amt = float(sys.argv[1])
    input_unit = sys.argv[2]
    output_unit = sys.argv[3]

    velocityConverter(amt, input_unit, output_unit)
