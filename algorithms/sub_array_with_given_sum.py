def get_sub_array_that_sums_to_target(target, array):
    current_sum = 0

    start = 0
    end = 0

    while end <= len(array):

        if current_sum == target:
            return array[start: end]

        if current_sum < target:
            current_sum += array[end]

            end += 1
        else:
            current_sum -= array[start]

            start += 1

    if current_sum == target:
        return array[start:end]
    else:
        return -1
