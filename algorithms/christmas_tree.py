def print_chrismas_tree(height):
    spaces = height
    asteriscs = 1

    for row in range(height):
        spaces_string = ' ' * spaces
        asteriscs_string = '*' * asteriscs

        print('{}{}'.format(spaces_string, asteriscs_string))

        spaces -= 1
        asteriscs += 2
