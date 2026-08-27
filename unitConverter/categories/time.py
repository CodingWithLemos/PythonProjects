# Time Module with Various Unit Conversions

# 1 year = 365.25 days

# main module
def main(conversion):
    #  function body
    def yearToNanosecond(t):
        nsec = t * 3.15576E16
        return nsec

    def yearToMillisecond(t):
        msec = t * 3.15576E10
        return msec

    def yearToSecond(t):
        sec = t * 3.15576E7
        return sec

    def yearToMinute(t):
        minute = t * 525960
        return minute

    def yearToHour(t):
        hour = t * 8766
        return hour

    def yearToDay(t):
        day = t * 365.25
        return day

    def dayToNanosecond(t):
        nsec = t * 8.64E13
        return nsec

    def dayToMillisecond(t):
        msec = t * 8.64E10
        return msec

    def dayToSecond(t):
        sec = t * 86400
        return sec

    def dayToMinute(t):
        minute = t * 1440
        return minute

    def dayToHour(t):
        hour = t * 24
        return hour

    def dayToYear(t):
        year = t / 365.25
        return year

    def hourToNanosecond(t):
        nsec = t * 3.6E12
        return nsec

    def hourToMillisecond(t):
        msec = t * 3.6E9
        return msec

    def hourToSecond(t):
        sec = t * 3600
        return sec

    def hourToMinute(t):
        minute = t * 60
        return minute

    def hourToDay(t):
        day = t / 24
        return day

    def hourToYear(t):
        year = t / 8766
        return year

    def minuteToNanosecond(t):
        nsec = t * 6E10
        return nsec

    def minuteToMillisecond(t):
        msec = t * 6E7
        return msec

    def minuteToSecond(t):
        sec = t * 60
        return sec

    def minuteToHour(t):
        hour = t / 60
        return hour

    def minuteToDay(t):
        day = t / 1440
        return day

    def minuteToYear(t):
        year = t / 525960
        return year

    def secondToNanosecond(t):
        nsec = t * 1E9
        return nsec
        
    def secondToMillisecond(t):
        msec = t * 1000
        return msec

    def secondToMinute(t):
        minute = t / 60
        return minute

    def secondToHour(t):
        hour = t / 3600
        return hour

    def secondToDay(t):
        day = t / 86400
        return day

    def secondToYear(t):
        year = t / 3.15576E7
        return year

    def millisecondToNanosecond(t):
        nsec = t * 1E6
        return nsec

    def millisecondToSecond(t):
        sec = t / 1000
        return sec

    def millisecondToMinute(t):
        minute = t / 6E4
        return minute

    def millisecondToHour(t):
        hour = t / 3.6E6
        return hour

    def millisecondToDay(t):
        day = t / 8.64E7
        return day

    def millisecondToYear(t):
        year = t / 3.15576E10
        return year

    def nanosecondToMillisecond(t):
        msec = t / 1E6
        return msec

    def nanosecondToSecond(t):
        sec = t / 1E9
        return sec

    def nanosecondToMinute(t):
        minute = t / 6E10
        return minute

    def nanosecondToHour(t):
        hour = t / 3.6E12
        return hour

    def nanosecondToDay(t):
        day = t / 8.64E13
        return day

    def nanosecondToYear(t):
        year = t / 3.15576E16
        return year

    # matching each function to conversion types input by user
    match conversion:
        case "year > nanosecond":
            print(f'Time in nanoseconds: {yearToNanosecond(t):.2f}')

        case "year > millisecond":
            print(f'Time in milliseconds: {yearToMillisecond(t):.2f}')

        case "year > second":
            print(f'Time in seconds: {yearToSecond(t):.2f}')

        case "year > minute":
            print(f'Time in minutes: {yearToMinute(t):.2f}')

        case "year > hour":
            print(f'Time in hours: {yearToHour(t):.2f}')

        case "year > day":
            print(f'Time in days: {yearToDay(t):.2f}')

        case "day > nanosecond":
            print(f'Time in nanoseconds: {dayToNanosecond(t):.2f}')

        case "day > millisecond":
            print(f'Time in milliseconds: {dayToMillisecond(t):.2f}')

        case "day > second":
            print(f'Time in seconds: {dayToSecond(t):.2f}')

        case "day > minute":
            print(f'Time in minutes: {dayToMinute(t):.2f}')

        case "day > hour":
            print(f'Time in hours: {dayToHour(t):.2f}')

        case "day > year":
            print(f'Time in years: {dayToYear(t):.2f}')

        case "hour > nanosecond":
            print(f'Time in nanoseconds: {hourToNanosecond(t):.2f}')

        case "hour > millisecond":
            print(f'Time in milliseconds: {hourToMillisecond(t):.2f}') 

        case "hour > second":
            print(f'Time in seconds: {hourToSecond(t):.2f}')

        case "hour > minute":
            print(f'Time in minutes: {hourToMinute(t):.2f}')   

        case "hour > day":
            print(f'Time in days: {hourToDay(t):.2f}')

        case "hour > year":
            print(f'Time in years: {hourToYear(t):.2f}')

        case "minute > nanosecond":
            print(f'Time in nanoseconds: {minuteToNanosecond(t):.2f}')

        case "minute > millisecond":
            print(f'Time in milliseconds: {minuteToMillisecond(t):.2f}')

        case "minute > second":
            print(f'Time in seconds: {minuteToSecond(t):.2f}')

        case "minute > hour":
            print(f'Time in hours: {minuteToHour(t):.2f}')

        case "minute > day":
            print(f'Time in days: {minuteToDay(t):.2f}')

        case "minute > year":
            print(f'Time in years: {minuteToYear(t):.2f}')

        case "second > nanosecond":
            print(f'Time in nanoseconds: {secondToNanosecond(t):.2f}')

        case "second > millisecond":
            print(f'Time in milliseconds: {secondToMillisecond(t):.2f}')

        case "second > minute":
            print(f'Time in minutes: {secondToMinute(t):.2f}')

        case "second > hour":
            print(f'Time in hours: {secondToHour(t):.2f}')

        case "second > day":
            print(f'Time in days: {secondToDay(t):.2f}')

        case "second > year":
            print(f'Time in years: {secondToYear(t):.2f}')

        case "millisecond > nanosecond":
            print(f'Time in nanoseconds: {millisecondToNanosecond(t):.2f}')

        case "millisecond > second":
            print(f'Time in seconds: {millisecondToSecond(t):.2f}')

        case "millisecond > minute":
            print(f'Time in minutes: {millisecondToMinute(t):.2f}')

        case "millisecond > hour":
            print(f'Time in hours: {millisecondToHour(t):.2f}')

        case "millisecond > day":
            print(f'Time in days: {millisecondToDay(t):.2f}')

        case "millisecond > year":
            print(f'Time in years: {millisecondToYear(t):.2f}')

        case "nanosecond > millisecond":
            print(f'Time in milliseconds: {nanosecondToMillisecond(t):.2f}')

        case "nanosecond > second":
            print(f'Time in seconds: {nanosecondToSecond(t):.2f}')

        case "nanosecond > minute":
            print(f'Time in minutes: {nanosecondToMinute(t):.2f}')

        case "nanosecond > hour":
            print(f'Time in hours: {nanosecondToHour(t):.2f}')

        case "nanosecond > day":
            print(f'Time in days: {nanosecondToDay(t):.2f}')

        case "nanosecond > year":
            print(f'Time in years: {nanosecondToYear(t):.2f}')
            
        case _:
            print("Invalid conversion!")    

if __name__ == "__main__":
    import sys
    t = float(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)