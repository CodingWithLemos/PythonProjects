# Time Module with Various Unit Conversions
# 1 year = 365.25 days

# function definition
def timeConverter(
        amt,
        input_unit,
        output_unit):
    
    """ prompt user to input time and conversion type, 
    then convert time to desired unit """

    match input_unit, output_unit:
        case 'years', 'hours':
            result = amt * 8766
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'hours', 'years':
            result = amt / 8766
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'years', 'minutes':
            result = amt * 525960
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'minutes', 'years':
            result = amt / 525960
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'hours', 'minutes':
            result = amt * 60
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'minutes', 'hours':
            result = amt / 60
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')
        
        case _:
            print('Invalid conversion!')

# main module
if __name__ == "__main__":
    import sys
    amt = float(sys.argv[1])
    input_unit = sys.argv[2]
    output_unit = sys.argv[3]

    timeConverter(amt, input_unit, output_unit)