def get_permutations_as_substring(small_string, big_string):
    """
    Given a small string, look for occurrences of permutations of this string in a biggest string
    """
    if big_string < small_string:
        return []

    permutations_found = []

    window_size = len(small_string)

    start = 0
    end = window_size

    while end <= len(big_string):
        substring = big_string[start:end]

        if _is_permutation_of(substring, small_string):
            if substring not in permutations_found:
                permutations_found.append(substring)

        start += 1
        end += 1

    return permutations_found


def _is_permutation_of(perm, string):
    list_perm = list(perm)
    list_string = list(string)

    list_perm.sort()
    list_string.sort()

    return list_perm == list_string



