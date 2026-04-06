'''
Write a function that counts the number of occurrences
of each element in a given list.
Once counted, print each element alongside the number of occurrences.
Consider the words case sensitive e.g. ("suv" != "SUV")
'''

def count_occurrences(lst):
    occurrences = {}
    for element in lst:
        occurrences[element] = occurrences.get(element, 0) + 1

    for key, value in occurrences.items():
        print(f"{key} => {value}")


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)