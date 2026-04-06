'''
Write a function that takes a string,
doubles every character in the string,
then returns the result as a new string.
'''

def repeater(text):
    result = ""
    for char in text:
        result += char * 2
    return result

def repeater(text):
    return ''.join(char * 2 for char in text)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True