'''
Write a function that takes a string,
doubles every consonant in the string,
and returns the result as a new string.
The function should not double vowels ('a','e','i','o','u'),
digits, punctuation, or whitespace
'''

def double_consonants(text):
    result = ''
    for char in text:
        if char in 'aeiouAEIOU' or not char.isalpha():
            result += char
        else:
            result += char * 2
    return result

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")