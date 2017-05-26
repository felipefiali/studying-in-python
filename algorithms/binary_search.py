
def do_binary_search(start, end, array, value):
    if start > end:
        return False

    mid = (start + end) // 2

    if array[mid] == value:
        return True

    if array[mid] > value:
        return do_binary_search(start, mid - 1, array, value)
    else:
        return do_binary_search(mid + 1, end, array, value)


def binary_search(array, value):
    start = 0
    end = len(array) - 1

    return do_binary_search(start, end, array, value)
