# Mass Module with Various Unit Conversions

# Main module

def main(conversion):
    # function body
    def kg_to_pounds(m):
        lbs = m * 2.20462
        return lbs

    def pounds_to_kg(m):
        kg = m / 2.20462
        return kg

    def kg_to_ounces(m):
        oz = m * 35.274
        return oz

    def ounces_to_kg(m):
        kg = m / 35.274
        return kg

    def pounds_to_ounces(m):
        oz = m * 16
        return oz

    def ounces_to_pounds(m):
        lbs = m / 16
        return lbs

# matching each function to conversion types input by user
    match conversion:
        case "kg > lbs":
            print(f"Mass in Pounds: {kg_to_pounds(m):.2f}")

        case "lbs > kg":
            print(f"Mass in Kilograms: {pounds_to_kg(m):.2f}")

        case "kg > oz":
            print(f"Mass in Ounces: {kg_to_ounces(m):.2f}")

        case "oz > kg":
            print(f"Mass in Kilograms: {ounces_to_kg(m):.2f}")

        case "lbs > oz":
            print(f"Mass in Ounces: {pounds_to_ounces(m):.2f}")

        case "oz > lbs":
            print(f"Mass in Pounds: {ounces_to_pounds(m):.2f}")

        case _:
            print("Invalid conversion!")


if __name__ == "__main__":
    import sys
    m = float(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)

