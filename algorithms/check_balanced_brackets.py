def check_if_brackets_are_balanced(brackets):
    """
    Checks if a string of brackets is balanced
    """
    if len(brackets) % 2 != 0:
        return False

    opening_chars = ['[', '(', '{']

    char_close_map = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    stack = []

    for char in brackets:
        if char in opening_chars:
            stack.append(char)
        else:
            last_opening = stack.pop()

            if char_close_map[last_opening] != char:
                return False

    if len(stack) > 0:
        return False

    return True




