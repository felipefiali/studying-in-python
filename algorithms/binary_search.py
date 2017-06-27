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


def find_item_in_rotated_sorted_array(array, low, high, target):
    if low == high:
        if array[low] == target:
            return low
        else:
            return -1

    mid = (low + high) // 2

    if array[mid] == target:
        return mid

    # Pivot point is at the right
    if array[low] <= array[mid]:
        if target >= array[low] and target <= array[mid]:
            return find_item_in_rotated_sorted_array(array, low, mid - 1, target)
        return find_item_in_rotated_sorted_array(array, mid + 1, high, target)

    # Pivot point is at the left
    if target >= array[mid] and target <= array[high]:
        return find_item_in_rotated_sorted_array(array, mid + 1, high, target)
    return find_item_in_rotated_sorted_array(array, low, mid - 1, target)
