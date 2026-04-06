'''
Write a function that takes a string argument
consisting of a first name, a space, and a last name.
The function should return a new string consisting
of the last name, a comma, a space, and the first name.
'''

def swap_name(full_name):
    name, surname = full_name.split()
    return f"{surname}, {name}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True