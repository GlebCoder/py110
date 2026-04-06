'''
Write a function that takes a time using this minute-based format
and returns the time of day in 24-hour format (hh:mm).
Your function should work with any integer input.
'''

def time_of_day(time):
    MINUTES_PER_DAY = 24 * 60
    minutes_after_midnight = time

    while minutes_after_midnight < 0:
        minutes_after_midnight += MINUTES_PER_DAY

    minutes_after_midnight %= MINUTES_PER_DAY
    hours = minutes_after_midnight // 60
    minutes = minutes_after_midnight % 60
    return f"{hours:02d}:{minutes:02d}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True