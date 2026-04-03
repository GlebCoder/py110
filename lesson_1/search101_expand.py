def is_bigger(lst, number):
    for num in lst:
        if num > number:
            return True
    return False

PROMPTS = [
            "==> Enter the 1st number: ",
            "==> Enter the 2nd number: ",
            "==> Enter the 3rd number: ",
            "==> Enter the 4th number: ",
            "==> Enter the 5th number: ",
]

numbers = []
for index in range(5):
    number = int(input(PROMPTS[index]))
    numbers.append(number)

last_number = int(input("==> Enter the last number: "))

num1, num2, num3, num4, num5 = numbers

if is_bigger(numbers, last_number):
    print(f"There is a bigger number than {last_number} in {num1},{num2},{num3},{num4},{num5}.")
else:
    print(f"There isn't a bigger number than {last_number} in {num1},{num2},{num3},{num4},{num5}.")