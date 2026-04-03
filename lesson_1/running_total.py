'''
Write a function that takes a list of numbers and
returns a list with the same number of elements,
but with each element's value being the running total from the original list.

Problem - i have a list with numbers, [1, 2, 3]
and i need to create a list with running totals [1, 1 + 2 = 3, 3 + 3 = 6]

Input - a list of numbers
Output - a list of numbers

Data - lists

Algorithm:
1. create variable total and assign it to 0
2. create variable running_total and assign it to empty list
3. Loop over the passed list and each time increase total by element of the list
4. Append total to running_total list
5. After the looping return the running_total
'''

def running_total(numbers):
    total = 0
    running_total = []
    for number in numbers:
        total += number
        running_total.append(total)
    return running_total

print(running_total([1, 2, 3]))
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True