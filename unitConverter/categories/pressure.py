# Pressure Module with Various Unit Conversions

# main module
def main(conversion):
    #  function body
    def pascalToBar(p):
        bar = p / 10000
        return bar

    def pascalToInchMercury(p):
        inhg = p / 3386
        return inhg

    def pascalToPsi(p):
        psi = p / 6895
        return psi

    def barToPascal(p):
        pascal = p * 10000
        return pascal

    def barToInchMercury(p):
        inhg = p * 29.53
        return inhg

    def barToPsi(p):
        psi = p * 14.5038
        return psi

    def inchMercuryToPascal(p):
        pascal = p * 3386
        return pascal

    def inchMercuryToBar(p):
        bar = p / 29.53
        return bar

    def inchMercuryToPsi(p):
        psi = p / 2.036
        return psi

    def psiToPascal(p):
        pascal = p * 6895
        return pascal

    def psiToInchMercury(p):
        inhg = p * 2.036
        return inhg

    def psiToBar(p):
        bar = p / 14.5038
        return bar


    # matching each function to conversion types input by user
    match conversion:
        case 'pascal > bar':
            print(f'Pressure in Bar: {pascalToBar(p):.2f}')
        case 'pascal > inchmercury':
            print(f'Pressure in Inch of Mercury: {pascalToInchMercury(p):.2f}')
        case 'pascal > psi':
            print(f'Pressure in Pound per Sq. Inch: {pascalToPsi(p):.2f}')
        case 'bar > pascal':
            print(f'Pressure in Pascal: {barToPascal(p):.2f}')
        case 'bar > inchmercury':
            print(f'Pressure in Inch of Mercury: {barToInchMercury(p):.2f}')
        case 'bar > psi':
            print(f'Pressure in Pound per Sq. Inch: {barToPsi(p):.2f}')
        case 'inchmercury > pascal':
            print(f'Pressure in Pascal: {inchMercuryToPascal(p):.2f}')
        case 'inchmercury > bar':
            print(f'Pressure in Bar: {inchMercuryToBar(p):.2f}')
        case 'inchmercury > psi':
            print(f'Pressure in Pound per Sq. Inch: {inchMercuryToPsi(p):.2f}')
        case 'psi > pascal':
            print(f'Pressure in Pascal: {psiToPascal(p):.2f}')
        case 'psi > inchmercury':
            print(f'Pressure in Inch of Mercury: {psiToInchMercury(p):.2f}')
        case 'psi > bar':
            print(f'Pressure in Bar: {psiToBar(p):.2f}')
        case _:
            print('Invalid conversion!')

if __name__ == "__main__":
    import sys
    p = float(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)