def maximize_cake_eating_pleasure(cake):
    cake_pleasure = 0

    cake_middle = (len(cake) - 1) // 2

    top_max = eat_from_the_top(cake[0:cake_middle + 1])
    bottom_max = eat_from_the_bottom(cake[cake_middle + 1:])

    if top_max > 0:
        cake_pleasure += top_max

    if bottom_max > 0:
        cake_pleasure += bottom_max

    return cake_pleasure


def eat_from_the_top(cake):
    maximum = 0
    cur = 0

    for number in cake:
        cur += number

        maximum = max(maximum, cur)

    return maximum


def eat_from_the_bottom(cake):
    maximum = 0
    cur = 0

    for number in reversed(cake):
        cur += number

        maximum = max(maximum, cur)

    return maximum
