def next_bigger_number(number):
    number_as_list = list(str(number))

    if len(number_as_list) < 2:
        return number

    for index in reversed(range(len(number_as_list) - 1)):
        if number_as_list[index] < number_as_list[index + 1]:
            number_to_switch = number_as_list[index]

            for bigger_than_index in reversed(range(len(number_as_list))):
                if index == bigger_than_index:
                    break

                if number_as_list[bigger_than_index] > number_to_switch:
                    number_as_list[index] = number_as_list[bigger_than_index]
                    number_as_list[bigger_than_index] = number_to_switch

                    number_as_list[index + 1:] = sorted(number_as_list[index + 1:])

                    return int(''.join(number_as_list))