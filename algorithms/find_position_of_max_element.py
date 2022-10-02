"""
 Given an array of integers, return the position of the maximum element.
 If the maximum element occurs multiple times, use a random number generator
 to choose one of the positions uniformly at random
"""
from random import randrange


def find_position_of_max_element(integers):
    max_index = None
    max_so_far = 0
    max_occurrences = 0

    for index, num in enumerate(integers):
        if num > max_so_far:
            max_so_far = num
            max_index = index
            max_occurrences = 1
        elif num == max_so_far:
            max_occurrences += 1

            if randrange(max_occurrences) == 0:
                max_index = index

    return max_index


