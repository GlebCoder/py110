'''
I am given a list of strings.
I have to sort the list based on the highest amount of adjacent
consonants.
Consonants are considered adjacent if they are next
to each other in the same word or
if there is a space between two consonants
in adjacent words (for example, "mpl", "t t")

Input - list of strings. Each string can contain
alphabetical characters and non-alphabetical characters.

Output - sorted list of strings.

Questions
1. Non-alphabetical characters only spaces or not?
2. Sorting - first element should be an element with
maximal amount of adjacent consonants?

Test examples:
According to the provided tests strings can be separate words
and words separated by spaces. There are no other symbols
such as question marks, dots, hyphens and so on...

Sorting should be done in descending order - first goes
an element with the highest amount of adjacent
consonants.

Case is not important. Strings cannot be empty.

Single consonant does not effect the sorting order.

Data Structure:
We have to use lists here. We will have an input list and
we should sort it and return the sorted list. I will assume
that we should not mutate the input list.

Algorithm:
1. Write a helper function that for takes a strig as an input
and returns number of adjacent consonants.
2. In the main function use built-in sorted function that will sort
the list of strings based on this helper function.

Now we need to write an algorithm for the helper function.
 - 1. Create a string of vowels to check if a character
 is vowel or consonant.
 - 2. Create a string which has all the characters from
 the original string without spaces
 - 3. Create a variable adjacent_consonants and assign it
 to 1.
 - 4. Create a variable max_adjacent_consonants and assign it
 to 1
 - 5. Check each character in the string without spaces.
 - 6. If a character is consonant and a previous character is consonant
 increase the variable adjacent_consonants by 1
 - 7. if max_adjacent_consonants is less than adjacent_consonants,
 assign max_adjacent_consonants to adjacent_consonants.
 - 8. If a character is vowel assign the variable adjacent_consonants
 to 1.
 - 9. Repeat 6, 7, 8
 - 10. Return max_adjacent_consonants.
'''

def max_adjacent_consonants(my_string):
    without_spaces = my_string.replace(' ', '')
    vowels = "aeiouAEIOU"
    adjacent_consonants = []
    max_adjacent = 0
    for char in without_spaces:
        if char not in vowels:
            adjacent_consonants.append(char)
            if max_adjacent < len(adjacent_consonants):
                max_adjacent = len(adjacent_consonants)
        else:
            adjacent_consonants.clear()
    return max_adjacent if max_adjacent > 1 else 0

print(max_adjacent_consonants('xxxx'))

def sort_by_consonant_count(my_list):
    return sorted(my_list, key=max_adjacent_consonants, reverse=True)


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']