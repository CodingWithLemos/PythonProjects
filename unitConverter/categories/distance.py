# Distance Module with Various Unit Conversions

# Main module
def main(conversion):
    # function body
    def kilometers_to_miles(d):
        miles = d / 1.60934
        return miles

    def kilometers_to_nautical_miles(d):
        nautical_miles = d / 1.852
        return nautical_miles

    def miles_to_kilometers(d):
        kilometers = d * 1.60934
        return kilometers

    def miles_to_nautical_miles(d):
        nautical_miles = d / 1.15078
        return nautical_miles

    def nautical_miles_to_kilometers(d):
        kilometers = d * 1.852
        return kilometers

    def nautical_miles_to_miles(d):
        miles = d * 1.15078
        return miles

    
# matching each function to conversion types input by user
    match conversion:
        case "km > mi":
            print(f"Distance in miles: {kilometers_to_miles(d):.2f}")

        case "km > nm":
            print(f"Distance in nautical miles: {kilometers_to_nautical_miles(d):.2f}")

        case "mi > km":
            print(f"Distance in kilometers: {miles_to_kilometers(d):.2f}")

        case "mi > nm":
            print(f"Distance in nautical miles: {miles_to_nautical_miles(d):.2f}")

        case "nm > km":
            print(f"Distance in kilometers: {nautical_miles_to_kilometers(d):.2f}")

        case "nm > mi":
            print(f"Distance in miles: {nautical_miles_to_miles(d):.2f}")

        case _:
            print("Invalid conversion!")

    
if __name__ == "__main__":
    import sys
    d = float(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)