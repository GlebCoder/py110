'''
Write two functions that each take a time of day in 24 hour format,
and return the number of minutes before and after midnight,
respectively. Both functions should return a value in the
range 0 through 1439
'''

MINUTES_PER_DAY = 60 * 24

def hours_minutes(time):
    hours, minutes = time.split(":")
    return int(hours), int(minutes)

def before_midnight(time):
    hours, minutes = hours_minutes(time)
    minutes_after_midnight = hours * 60 + minutes
    minutes_after_midnight %= MINUTES_PER_DAY
    return 0 if minutes_after_midnight == 0 else MINUTES_PER_DAY - minutes_after_midnight

def after_midnight(time):
    hours, minutes = hours_minutes(time)
    minutes_after_midnight = hours * 60 + minutes
    minutes_after_midnight %= MINUTES_PER_DAY
    return minutes_after_midnight


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True