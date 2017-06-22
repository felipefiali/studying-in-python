def longest_increasing_sub_array(array):
    if array is None or len(array) < 1:
        return array

    best_start = 0
    best_end = 0

    start = 0
    end = 1

    while end < len(array):
        if array[end] < array[end - 1]:
            start = end

        current_size = (end - start) + 1
        best_size = (best_end - best_start) + 1

        if current_size > best_size:
            best_start = start
            best_end = end

        end += 1

    return array[best_start:best_end + 1]