def count_occurrences_ordered_array(array, n):
    return do_count_occurrences_ordered_array(array, n, 0, len(array) - 1)


def do_count_occurrences_ordered_array(array, n, low, high):
    if low > high:
        return 0

    if low == high:
        if array[low] == n:
            return 1
        else:
            return 0

    mid = (low + high) // 2

    current = 0

    if array[mid] == n:
        current += 1

        current += do_count_occurrences_ordered_array(array, n, low, mid - 1)
        current += do_count_occurrences_ordered_array(array, n, mid + 1, high)

        return current

    if array[mid] > n:
        return do_count_occurrences_ordered_array(array, n, low, mid - 1)
    else:
        return do_count_occurrences_ordered_array(array, n, mid + 1, high)


