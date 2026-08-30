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