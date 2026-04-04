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

def signed_integer_to_string(num):
    if num < 0:
        return "-" + integer_to_string(abs(num))
    if num > 0:
        return "+" + integer_to_string(abs(num))
    return "0"

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True