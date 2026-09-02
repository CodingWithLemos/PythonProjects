# Unit Converter Main Python Program

# Imports Section
import sys

from categories.distance import distanceConverter
from categories.fuelecon import fuelConverter
from categories.mass import massConverter
from categories.pressure import pressureConverter
from categories.temperature import temperatureConverter
from categories.time import timeConverter
from categories.velocity import velocityConverter

def main():
    # Function Definition Section
    def menu():
        print('1. Convert Distance\n2. Convert Fuel Economy\n3. Convert Mass\n'
        '4. Convert Pressure\n5. Convert Temperature\n6. Convert Time\n' 
        '7. Convert Velocity\n8. Exit to Terminal')

    def convert_distance():
        amt = float(input('(1/3) Type an amount to be converted, such as 25.\n'))
        input_unit = input('(2/3) Type a unit to convert from, such as miles.\n')
        output_unit = input('(3/3) Type a unit to convert to, such as kilometers.\n')

        distanceConverter(amt, input_unit, output_unit)

    def convert_fuel():
        amt = float(input('(1/3) Type an amount to be converted, such as 25.\n'))
        input_unit = input('(2/3) Type a unit to convert from, such as miles per gallon.\n')
        output_unit = input('(3/3) Type a unit to convert to, such as kilometers per liter.\n')

        fuelConverter(amt, input_unit, output_unit)

    def convert_mass():
        amt = float(input('(1/3) Type an amount to be converted, such as 25.\n'))
        input_unit = input('(2/3) Type a unit to convert from, such as pounds.\n')
        output_unit = input('(3/3) Type a unit to convert to, such as ounces.\n')

        massConverter(amt, input_unit, output_unit)

    def convert_pressure():
        amt = float(input('(1/3) Type an amount to be converted, such as 25.\n'))
        input_unit = input('(2/3) Type a unit to convert from, such as hectopascal.\n')
        output_unit = input('(3/3) Type a unit to convert to, such as bar.\n')

        pressureConverter(amt, input_unit, output_unit)

    def convert_temperature():
        amt = float(input('(1/3) Type an amount to be converted, such as 25.\n'))
        input_unit = input('(2/3) Type a unit to convert from, such as celsius.\n')
        output_unit = input('(3/3) Type a unit to convert to, such as fahrenheit.\n')

        temperatureConverter(amt, input_unit, output_unit)

    def convert_time():
        amt = float(input('(1/3) Type an amount to be converted, such as 25.\n'))
        input_unit = float(input('(2/3) Type a unit to convert from, such as years.\n'))
        output_unit = float(input('(3/3) Type a unit to convert to, such as minutes.\n'))

        timeConverter(amt, input_unit, output_unit)

    def convert_velocity():
        amt = float(input('(1/3) Type an amount to be converted, such as 25.\n'))
        input_unit = input('(2/3) Type a unit to convert from, such as miles per hour.\n')
        output_unit = input('(3/3) Type a unit to convert to, such as knots.\n')

        velocityConverter(amt, input_unit, output_unit)

    def exit_to_terminal(prompt='Are you sure you want to exit? y/n\n'):
        confirm = input(prompt)

        if confirm in ('y', 'Y', 'yes', 'yea'):
            print('Goodbye!')
            sys.exit(0)
        elif confirm in ('n', 'N', 'no', 'nay'):
            pass
        else:
            exit_to_terminal("I'm sorry, I did not understand that. Please type \'yes\' or \'no\'\n.")

    # program loop
    print('Welcome to the unit converter Python program!')

    while True:
        try:
            menu()
            option_selection = int(input('Select an option 1-8 to continue.\n'))

        except:
            print('Invalid option! Select an option 1-8 to continue.')
        
        match option_selection:
            case 1:
                convert_distance()

            case 2:
                convert_fuel()

            case 3:
                convert_mass()

            case 4:
                convert_pressure()

            case 5:
                convert_temperature()

            case 6:
                convert_time()

            case 7:
                convert_velocity()

            case 8:
                exit_to_terminal()

            case _:
                print('Invalid option! Select an option 1-8 to continue.')

# Main program
if __name__ == '__main__':
    main()

