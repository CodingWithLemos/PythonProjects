# Length Module with Various Unit Conversions

# Main module
def main(conversion):

    def kilometers_to_miles(d):
        miles = d / 1.60934
        return miles

    def kilometers_to_nauticle_miles(d):
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
    
if __name__ == "__main__":
    import sys
    d = float(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)