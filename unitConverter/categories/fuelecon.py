# Fuel Economy Module with Various Unit Conversions

# function definition
def fuelConverter(
        amt,
        input_unit,
        output_unit):
    
    """ prompt user to input fuel economy and conversion type, 
    then convert fuel economy to desired unit """

    match input_unit, output_unit:
        case 'liters per 100km', 'miles per gallon':
            result = 235.215 / amt
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'miles per gallon', 'liters per 100km':
            result = 235.215 / amt
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'liters per 100km', 'kilometers per liter':
            result = 100 / amt
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'kilometers per liter', 'liters per 100km':
            result = 100 / amt
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'miles per gallon', 'kilometers per liter':
            result = amt / 2.35215
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')

        case 'kilometers per liter', 'miles per gallon':
            result = amt * 2.35215
            print(f'{amt:.2f} {input_unit} is equal to {result:.2f} {output_unit}.')
        
        case _:
            print('Invalid conversion!')

# main module
if __name__ == "__main__":
    import sys
    amt = float(sys.argv[1])
    input_unit = sys.argv[2]
    output_unit = sys.argv[3]

    fuelConverter(amt, input_unit, output_unit)