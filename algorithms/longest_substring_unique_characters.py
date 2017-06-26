def get_longest_substring_with_unique_characters(value):
    if value is None or value == '' or len(value) <= 1:
        return value

    characters_hash_table = []

    best_start = 0
    best_end = 0

    end = 0
    start = 0

    while end < len(value):
        if value[end] not in characters_hash_table:
            characters_hash_table.append(value[end])

            cur_size = end - start
            best_size = best_end - best_start

            if cur_size > best_size:
                best_start = start
                best_end = end
        else:
            start = end

        end += 1

    return value[best_start:best_end + 1]


