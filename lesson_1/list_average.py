'''
Write a function that takes one argument, a list of integers,
and returns the average of all the integers in the list,
rounded down to the integer component of the average.
The list will never be empty,
and the numbers will always be positive integers.
'''

def average(numbers):
    return int(sum(numbers) / len(numbers))