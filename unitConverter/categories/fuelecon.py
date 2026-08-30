# Fuel Economy Module with Various Unit Conversions

# Main module

def main(conversion):
    # function body
    def liters_per_100km_to_miles_per_gallon(f):
        mpg = 235.215 / f
        return mpg

    def miles_per_gallon_to_liters_per_100km(f):
        l_per_100km = 235.215 / f
        return l_per_100km

    def kilometers_per_liter_to_miles_per_gallon(f):
        mpg = f * 2.35215
        return mpg

    def miles_per_gallon_to_kilometers_per_liter(f):
        km_per_liter = f / 2.35215
        return km_per_liter

    def liters_per_100km_to_kilometers_per_liter(f):
        km_per_liter = 100 / f
        return km_per_liter

    def kilometers_per_liter_to_liters_per_100km(f):
        l_per_100km = 100 / f
        return l_per_100km

# matching each function to conversion types input by user
    match conversion:
        case "L100km > mpg":
            print(f"Fuel Economy in miles per gallon: {liters_per_100km_to_miles_per_gallon(f):.2f}")

        case "mpg > L100km":
            print(f"Fuel Economy in liters per 100 kilometers: {miles_per_gallon_to_liters_per_100km(f):.2f}")

        case "kmL > mpg":
            print(f"Fuel Economy in miles per gallon: {kilometers_per_liter_to_miles_per_gallon(f):.2f}")

        case "mpg > kmL":
            print(f"Fuel Economy in kilometers per liter: {miles_per_gallon_to_kilometers_per_liter(f):.2f}")

        case "L100km > kmL":
            print(f"Fuel Economy in kilometers per liter: {liters_per_100km_to_kilometers_per_liter(f):.2f}")

        case "kmL > L100km":
            print(f"Fuel Economy in liters per 100 kilometers: {kilometers_per_liter_to_liters_per_100km(f):.2f}")

if __name__ == "__main__":
    import sys
    f = float(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)