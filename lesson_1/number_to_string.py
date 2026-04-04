'''
Write a function that converts a non-negative integer value
(e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python,
such as str. Your function should do this the old-fashioned way and construct
the string by analyzing and manipulating the number.
'''

def integer_to_string(num):
    digits = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }
    str_num = ""
    current_num = num
    while current_num > 0:
        current_num, digit = divmod(current_num, 10)
        str_num = digits[digit] + str_num
    return str_num or "0"

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == '0')                    # True
print(integer_to_string(5500))              # True
print(integer_to_string(1234567890))  # True