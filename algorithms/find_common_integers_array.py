def find_common_integers_sorted_arrays(array1, array2):
    """
    Finds the common integer numbers in two sorted arrays
    """
    array1_pointer = 0
    array2_pointer = 0

    common_numbers = []

    while array1_pointer < len(array1) and array2_pointer < len(array2):
        if array1[array1_pointer] == array2[array2_pointer]:
            common_numbers.append(array1[array1_pointer])

            array1_pointer += 1
            array2_pointer += 1
        elif array1[array1_pointer] < array2[array2_pointer]:
            array1_pointer += 1
        else:
            array2_pointer += 1

    return common_numbers


def find_common_integers_unsorted_arrays(array1, array2):
    """
    Finds the common integer numbers in two unsorted arrays
    """
    if len(array1) > len(array2):
        array_to_iterate = array2
        array_to_compare = array1
    else:
        array_to_iterate = array1
        array_to_compare = array2

    common_numbers = []

    for num in array_to_iterate:
        if num in array_to_compare:
            common_numbers.append(num)

    return common_numbers
