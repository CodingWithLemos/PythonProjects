# Velocity Module with Various Unit Conversions

# Main module

def main(conversion):
    # function body
    def km_per_hour_to_mi_per_hour(v): 
        mph = v / 1.60934
        return mph

    def km_per_hour_to_knots(v):
        knots = v / 1.852
        return knots

    def mi_per_hour_to_km_per_hour(v):
        kmh = v * 1.60934
        return kmh
    
    def mi_per_hour_to_knots(v):
        knots = v / 1.15078
        return knots
    
    def knots_to_km_per_hour(v):
        kmh = v * 1.852
        return kmh
    
    def knots_to_mi_per_hour(v):
        mph = v * 1.15078
        return mph
    
# matching each function to conversion types input by user
    match conversion:
        case 'kmh > mph':
            print(f'Velocity in Miles per Hour: {km_per_hour_to_mi_per_hour(v):.2f}')

        case 'kmh > kts':
            print(f'Velocity in Knots: {km_per_hour_to_knots(v):.2f}')

        case 'mph > kmh':
            print(f'Velocity in Kilometers per Hour: {mi_per_hour_to_km_per_hour(v):.2f}')

        case 'mph > kts':
            print(f'Velocity in Knots: {mi_per_hour_to_knots(v):.2f}')

        case 'kts > kmh':
            print(f'Velocity in Kilometers per Hour: {knots_to_km_per_hour(v):.2f}')

        case 'kts > mph':
            print(f'Velocity in Miles per Hour: {knots_to_mi_per_hour(v):.2f}')

        case _:
            print('Invalid conversion!')

if __name__ == "__main__":
    import sys
    v = float(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)
