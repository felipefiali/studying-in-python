def get_edit_distance(string1, string2):
    table_height = len(string1) + 1
    table_width = len(string2) + 1

    table = [[0 for width in range(table_width)] for height in range(table_height)]

    for i in range(len(table[0])):
        table[0][i] = i

    for i in range(len(table)):
        table[i][0] = i

    for x in range(1, len(string1) + 1):
        for y in range(1, len(string2) + 1):
            if string1[x - 1] == string2[y - 1]:
                table[x][y] = table[x - 1][y - 1]
            else:
                table[x][y] = 1 + min([table[x - 1][y - 1], table[x - 1][y], table[x][y - 1]])

    print_edits(table, string1, string2)

    return table[len(string1)][len(string2)]


def print_edits(table, string1, string2):
    x = len(table) - 1
    y = len(table[0]) - 1

    while True:
        if x == 0 or y == 0:
            break

        if string1[x - 1] == string2[y - 1]:
            x -= 1
            y -= 1
        elif table[x][y] == table[x - 1][y - 1] + 1:
            print('Edit {}[{}] in string2 to {}[{}] in string 1'.format(string2[y - 1], y - 1, string1[x - 1], x - 1))
            x -= 1
            y -= 1
        elif table[x][y] == table[x - 1][y] + 1:
            print('Delete in string 1 {}[{}]'.format(string1[x - 1], x - 1))
            x -= 1
        elif table[x][y] == table[x][y - 1] + 1:
            print('Delete in string2 {}[{}]'.format(string2[y - 1], y - 1))
            y -= 1
        else:
            print('ERROR!!')
