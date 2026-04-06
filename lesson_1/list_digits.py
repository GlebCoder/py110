'''
Write a function that takes one argument,
a positive integer, and returns a list of the digits in the number.
'''

def digit_list(number):
    result = []
    while number > 0:
        number, digit = divmod(number, 10)
        result = [digit] + result
    return result

def digit_list(number):
    return [int(a) for a in str(number)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True