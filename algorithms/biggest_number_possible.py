def biggest_number_possible(number):
    if number == 0:
        return number

    string_list = list(str(number))

    string_list.sort(reverse=True)

    return int(''.join(string_list))
