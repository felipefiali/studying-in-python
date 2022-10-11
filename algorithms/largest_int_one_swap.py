"""
Get the largest int with one swap.

Example:
    52341 -> 54321
    7238  -> 8237
"""


def get_largest_int_with_one_swap(number):
    if number < 10:
        return number

    target_swap = 0
    source_swap = -1
    largest_number = -1
    largest_number_index = -1

    num_str = list(str(number))

    for i in range(len(num_str) - 1, -1, -1):
        if int(num_str[i]) >= int(largest_number):
            largest_number_index = i
            largest_number = num_str[i]
        else:
            target_swap = i
            source_swap = largest_number_index

    if source_swap > -1:
        temp = num_str[target_swap]
        num_str[target_swap] = num_str[source_swap]
        num_str[source_swap] = temp

    return int(''.join(num_str))


