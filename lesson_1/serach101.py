'''
I have to ask a user to enter six numbers
and check if a sixth number already is in the first
5 numbers.
Input - I will get numbers one by one from a user in a form
of strings.
Output - I will print a string as an answer: "The number
is/isn't in number1, number2, etc."
Testing examples show only positive integers. I do not think
that it's important for this task.

Data - I will put first 5 numbers in a list.

Algorithm:
1. Create an empty list for 5 first numbers
2. Ask a user to enter a number
3. Write this number in a list
4. Repeat steps 2 and 3 until we have 5 numbers in the list
5. Ask the user to enter the sixth number.
6. Check if this number already in the list.
7. Print the answer.
'''
PROMPTS = [
            "==> Enter the 1st number: ",
            "==> Enter the 2nd number: ",
            "==> Enter the 3rd number: ",
            "==> Enter the 4th number: ",
            "==> Enter the 5th number: ",
]

numbers = []
for index in range(5):
    number = input(PROMPTS[index])
    numbers.append(number)

last_number = input("==> Enter the last number: ")

if last_number in numbers:
    print(f"{last_number} is in {','.join(numbers)}.")
else:
    print(f"{last_number} isn't in {','.join(numbers)}.")
