def shortest_substring_with_strings_smart_approach(input_string, substring_list):
    if not all_substrings_present(substring_list, input_string, 0, len(input_string)):
        return ''

    best_start = 0
    best_end = len(input_string) - 1

    start = 0

    for end in range(len(input_string)):
        if all_substrings_present(substring_list, input_string, start, end):
            best_start = start
            best_end = end

            while start < end:
                start += 1

                if all_substrings_present(substring_list, input_string, start, end):
                    best_start = start
                else:
                    break

    return input_string[best_start:best_end]


def shortest_substring_with_strings_brute_force(input_string, substring_list):
    if not all_substrings_present(substring_list, input_string, 0, len(input_string)):
        return ''

    best_so_far = len(input_string)
    best_start = 0
    best_end = 0

    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string), 1):
            if all_substrings_present(substring_list, input_string, start, end):
                if (end - start) < best_so_far:
                    best_so_far = end - start
                    best_start = start
                    best_end = end

    return input_string[best_start:best_end]


def all_substrings_present(substring_list, sample_input, start, end):
    return all(substring in sample_input[start:end] for substring in substring_list)
