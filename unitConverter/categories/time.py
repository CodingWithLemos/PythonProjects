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

if __name__ == "__main__":
    import sys
    t = float(sys.argv[1])
    conversion = sys.argv[2]
    main(conversion)