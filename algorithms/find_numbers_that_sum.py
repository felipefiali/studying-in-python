def check_for_sum_in_two_unique_numbers(array, target):
    """
    Given an array of unique integers, and a target T, check if it is possible to reach that value
    with two unique numbers in the array.
    """

    hash_table = {}

    for index, number in enumerate(array):
        hash_table[number] = True

    for number in hash_table:
        diff = target - number

        if diff == number:
            continue

        if diff in hash_table:
            return True

    return False


def check_for_sum_in_two_numbers(array, target):
    """
    Given an array of integers that may be repeated in the array itself, check if it is possible to reach a value with
    two numbers in the array.
    """

    hash_table = {}

    for number in array:
        if number not in hash_table:
            hash_table[number] = 1
        else:
            hash_table[number] += 1

    for number in hash_table:
        diff = target - number

        if diff in hash_table:
            if diff == number:
                if hash_table[diff] >= 2:
                    return True
            else:
                return True

    return False


def check_for_sum_in_three_numbers(array, target):
    """
    Given an array of integers, find if there is a combination of three numbers that can reach to a target.
    The combination can be three different numbers, twice a number and a different one, or three times the same number.
    """

    hash_table = {}

    for number in array:
        if number * 3 == target:
            return True

        hash_table[number] = True

    for first_number in hash_table:
        if first_number < target:
            for second_number in hash_table:
                if first_number + second_number > target:
                    continue

                diff = target - (first_number + second_number)

                if diff in hash_table:
                    return True

    return False
