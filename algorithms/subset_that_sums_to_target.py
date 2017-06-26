def has_subset_that_sums(array, target):
    table = [[0 for rows in range(len(array) + 1)] for cols in range(target + 1)]

    for row in range(len(table)):
        table[row][0] = True

    for col in range(len(table[0])):
        table[0][col] = False

    for row in range(1, len(array) + 1):
        for col in range(1, target + 1):
            table[row][col] = table[row - 1][col]

            if not table[row][col] and col >= array[row - 1]:
                table[row][col] = table[row][col] or table[row - 1][col - array[row - 1]]

    return table[len(array)][target]
