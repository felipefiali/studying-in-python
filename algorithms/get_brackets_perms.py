results = []
num = 0


def get_brackets_perms(n):
    global num

    num = n * 2

    _add_brackets_recursively(n, n, [None] * num)

    return results


def _add_brackets_recursively(left, right, current):
    if left == 0 and right == 0:
        results.append(''.join(current))
        return

    pos = num - left - right

    if left > 0:
        current[pos] = '('

        _add_brackets_recursively(left - 1, right, current)

    if left < right:
        current[pos] = ')'

        _add_brackets_recursively(left, right - 1, current)
