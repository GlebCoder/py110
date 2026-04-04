'''
Write a function that takes a string of digits
and returns the appropriate number as an integer.
You may not use any of the standard conversion functions available in Python,
such as int. Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs,
nor should you worry about invalid characters; assume all characters are numeric.
'''

digits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

def string_to_integer(s):
    result = 0
    for index, char in enumerate(s):
        multiplier = 10 ** (len(s) - 1 - index)
        result += multiplier * digits[char]

    return result

print(string_to_integer("4321"))  # True
print(string_to_integer("570") == 570)    # True