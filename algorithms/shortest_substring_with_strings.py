def shortest_substring_with_strings_brute_force(input_string, substring_list):
    if not check_if_all_substrings_are_present(substring_list, input_string, 0, len(input_string)):
        return ''

    best_so_far = len(input_string)
    best_start = 0
    best_end = 0

    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string), 1):
            if check_if_all_substrings_are_present(substring_list, input_string, start, end):
                if (end - start) < best_so_far:
                    best_so_far = end - start
                    best_start = start
                    best_end = end

    return input_string[best_start:best_end]


def check_if_all_substrings_are_present(substring_list, sample_input, start, end):
    return all(substring in sample_input[start:end] for substring in substring_list)