"""
Remove the minimum number of parentheses from a string to make it valid.
"""


def remove_min_parentheses(invalid_string):
    if invalid_string is None or len(invalid_string) == 0:
        return invalid_string

    open_stack = []
    resulting_string = []

    for char in invalid_string:
        if char == '(':
            open_stack.append(char)
            resulting_string.append(char)
        elif char == ')':
            if len(open_stack) == 0:
                continue
            else:
                open_stack.pop()
                resulting_string.append(char)
        else:
            resulting_string.append(char)

    while len(open_stack) != 0:
        resulting_string.remove(open_stack.pop())

    return ''.join(resulting_string)



