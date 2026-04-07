'''
Write a function that takes a string as an argument
and returns True if all parentheses in the string
are properly balanced, False otherwise.
To be properly balanced, parentheses must occur
in matching '(' and ')' pairs.
'''

def is_balanced(text):
    count = 0
    for char in text:
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True