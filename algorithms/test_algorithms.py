from unittest import TestCase
from algorithms.binary_search import *
from algorithms.find_numbers_that_sum import *
from algorithms.cake_eating_problem import *
from algorithms.merge_ordered_arrays import *
from algorithms.christmas_tree import *
from algorithms.heap_sort import *
from data_structures.queue_with_stacks import *
from data_structures.trie import *
from data_structures.lru import LRUCache
from data_structures.binary_tree import *
from data_structures.min_heap import *
from algorithms.shortest_substring_with_strings import *
from algorithms.longest_increasing_sub_array import *
from algorithms.biggest_number_possible import *
from algorithms.next_bigger_number import *
from algorithms.string_edit_distance import *
from algorithms.longest_substring_unique_characters import *
from algorithms.sub_array_with_given_sum import *
from algorithms.subset_that_sums_to_target import *
from algorithms.get_brackets_perms import *
from algorithms.find_path_between_nodes import *
from algorithms.count_occurrences_ordered_array import *
from algorithms.people_alive_year import *
from algorithms.find_common_integers_array import *
from algorithms.check_balanced_brackets import *
from algorithms.find_average_on_level_binary_tree import *
from algorithms.find_position_of_max_element import *
from algorithms.meeting_rooms_required import *
from algorithms.largest_int_one_swap import *
from permutation_as_substring import *
from task_queue import *
from check_palindrome_removing_1_char import *


class TestAlgorithms(TestCase):
    def test_binary_search(self):
        ordered_array = [6, 8, 9, 11, 15]

        self.assertTrue(binary_search(ordered_array, 6))
        self.assertTrue(binary_search(ordered_array, 8))
        self.assertTrue(binary_search(ordered_array, 9))
        self.assertTrue(binary_search(ordered_array, 11))
        self.assertTrue(binary_search(ordered_array, 15))

        self.assertFalse(binary_search(ordered_array, -9))
        self.assertFalse(binary_search(ordered_array, 20.5))
        self.assertFalse(binary_search(ordered_array, 1000))

    def test_queue_with_stacks(self):
        queue = QueueWithStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

    def test_check_for_sum_in_two_unique_numbers(self):
        self.assertTrue(check_for_sum_in_two_unique_numbers([100, 48, 52], 100))
        self.assertFalse(check_for_sum_in_two_unique_numbers([100], 100))
        self.assertFalse(check_for_sum_in_two_unique_numbers([100, 50, 20], 80))
        self.assertFalse(check_for_sum_in_two_unique_numbers([], 100))

    def test_check_for_sum_in_two_numbers(self):
        self.assertTrue(check_for_sum_in_two_numbers([100, 48, 52], 100))
        self.assertTrue(check_for_sum_in_two_numbers([100, 100, 99, 1], 200))
        self.assertFalse(check_for_sum_in_two_numbers([100], 100))
        self.assertFalse(check_for_sum_in_two_numbers([100, 99], 200))
        self.assertFalse(check_for_sum_in_two_numbers([], 100))

    def test_check_for_sum_in_three_numbers(self):
        self.assertTrue(check_for_sum_in_three_numbers([100], 300))
        self.assertTrue(check_for_sum_in_three_numbers([99, 100, 30, 10], 300))
        self.assertTrue(check_for_sum_in_three_numbers([100, 100], 300))
        self.assertTrue(check_for_sum_in_three_numbers([25, 20], 70))
        self.assertTrue(check_for_sum_in_three_numbers([1, 2, 3, 4, 5, 6], 7))

        self.assertFalse(check_for_sum_in_three_numbers([], 100))
        self.assertFalse(check_for_sum_in_three_numbers([1, 2, 3, 4, 5, 6], 100))

    def test_maximize_cake_eating_pleasure(self):
        self.assertEqual(14, maximize_cake_eating_pleasure([10, -2, 5, -4, 3, -5, 1]))
        self.assertEqual(27, maximize_cake_eating_pleasure([-1, -5, -7, 9, 10, 8]))
        self.assertEqual(0, maximize_cake_eating_pleasure([-1, -2, 1, -7]))

    def test_merge_ordered_arrays_happy_path(self):
        array_1 = [1, 9]
        array_2 = [2, 8]
        array_3 = [1, 10]

        expected_array = [1, 1, 2, 8, 9, 10]

        self.assertSequenceEqual(expected_array, merge_ordered_arrays([array_1, array_2, array_3]))

    def test_merge_ordered_arrays_one_ends_sooner(self):
        array_1 = [1, 1, 1]
        array_2 = [4, 10]
        array_3 = [5, 11]

        expected_array = [1, 1, 1, 4, 5, 10, 11]

        self.assertSequenceEqual(expected_array, merge_ordered_arrays([array_1, array_2, array_3]))

    def test_merge_ordered_arrays_same_integers(self):
        array_1 = [1, 1]
        array_2 = [1, 1]
        array_3 = [1, 1]

        expected_array = [1, 1, 1, 1, 1, 1]

        self.assertSequenceEqual(expected_array, merge_ordered_arrays([array_1, array_2, array_3]))

    def test_merge_ordered_arrays_empty_list(self):
        self.assertSequenceEqual([], merge_ordered_arrays([]))

    def test_trie_suggestions(self):
        trie = Trie()

        trie.insert('car')
        trie.insert('carry')
        trie.insert('carrier')
        trie.insert('carbone')
        trie.insert('carb')
        trie.insert('ball')
        trie.insert('bee')
        trie.insert('baller')
        trie.insert('balloon')

        expected_suggestions = ['bee', 'ball', 'balloon', 'baller']

        self.assertEqual(expected_suggestions, trie.lookup('b'))

        expected_suggestions = ['ball', 'balloon', 'baller']

        self.assertListEqual(expected_suggestions, trie.lookup('ba'))

        expected_suggestions = ['bee']

        self.assertListEqual(expected_suggestions, trie.lookup('be'))

    def test_christmas_tree(self):
        print_chrismas_tree(5)

    def test_shortest_substring_brute_force(self):
        actual_shortest = shortest_substring_with_strings_brute_force('this is a big string', ['big', 'str', 'a'])
        expected_shortest = 'a big str'

        self.assertEqual(expected_shortest, actual_shortest)

    def test_shortest_string_smart(self):
        input_string = 'this is a biga string'
        substring_list = ['this', 'is']

        expected_shortest = 'this'

        actual_shortest = shortest_substring_with_strings_smart_approach(input_string, substring_list)

        self.assertEqual(expected_shortest, actual_shortest)

    def test_shortest_string_smart_multiple(self):
        input_string = 'abcfaeecb'
        substring_list = ['a', 'b', 'c']

        expected_shortest = 'abc'

        actual_shortest = shortest_substring_with_strings_smart_approach(input_string, substring_list)

        self.assertEqual(expected_shortest, actual_shortest)

    def test_longest_increasing_sub_array(self):
        self.assertSequenceEqual([1, 2, 3, 4], longest_increasing_sub_array([1, 2, 3, 1, 2, 3, 4]))
        self.assertSequenceEqual([1, 9, 10], longest_increasing_sub_array([1, 9, 10, 1]))
        self.assertSequenceEqual([1, 2], longest_increasing_sub_array([1, 2]))
        self.assertSequenceEqual([1, 1], longest_increasing_sub_array([1, 1]))
        self.assertSequenceEqual([1], longest_increasing_sub_array([1, 0]))

    def test_get_biggest_number(self):
        self.assertEqual(977321, biggest_number_possible(719273))

    def test_get_next_bigger_number(self):
        self.assertEqual(426238, next_bigger_number(423862))
        self.assertEqual(121, next_bigger_number(112))

    def test_get_string_edit_distance(self):
        self.assertEqual(4, get_edit_distance('esse aqui eh um exemplo', 'esse aqui eh outro exemplo'))

    def test_lru_cache_discards_on_put(self):
        lru = LRUCache(3)

        lru.put(1, 10)
        lru.put(2, 10)
        lru.put(3, 10)

        lru.put(4, 10)

        self.assertTrue(1 not in lru.items)

        lru.put(5, 10)

        self.assertTrue(2 not in lru.items)

    def test_lru_cache_prioritizes_on_get(self):
        lru = LRUCache(3)

        lru.put(1, 10)
        lru.put(2, 10)
        lru.put(3, 10)

        lru.get(1)

        lru.put(4, 10)

        self.assertTrue(2 not in lru.items)

    def test_get_longest_substring_unique_chars(self):
        input_string = 'abcddefghij'

        expected_value = 'defghij'

        self.assertEqual(expected_value, get_longest_substring_with_unique_characters(input_string))

    def test_get_sub_array_with_given_sum(self):
        target = 8

        self.assertSequenceEqual([3, 5], get_sub_array_that_sums_to_target(target, [1, 3, 5, 10, 11]))
        self.assertSequenceEqual([8], get_sub_array_that_sums_to_target(target, [1, 99, 8]))

    def test_can_subset_sum(self):
        self.assertTrue(has_subset_that_sums([1, 2, 3], 3))
        self.assertFalse(has_subset_that_sums([99, 2, 2], 3))

    def test_find_item_in_rotated_sorted_array(self):
        rotated_array = [7, 8, 9, 1, 2, 3, 4]
        target = 8

        self.assertEqual(1, find_item_in_rotated_sorted_array(rotated_array, 0, len(rotated_array) - 1, target))

    def test_add_brackets_recursively(self):
        actual = get_brackets_perms(3)

        expected = ['((()))', '(()())', '(())()', '()(())', '()()()']

        self.assertSequenceEqual(actual, expected)

    def test_heap_sort(self):
        self.assertSequenceEqual(heap_sort([5, 8, 1, 2, 5, 9, 0]), [0, 1, 2, 5, 5, 8, 9])
        self.assertSequenceEqual(heap_sort([5]), [5])
        self.assertSequenceEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertSequenceEqual(heap_sort([]), [])

    def test_find_path_nodes(self):
        nodes_tuples = []

        expected = ['B', 'T', 'G', 'P', 'M']

        nodes_tuples.append(('G', 'P'))
        nodes_tuples.append(('B', 'T'))
        nodes_tuples.append(('P', 'M'))
        nodes_tuples.append(('T', 'G'))

        start = 'B'
        end = 'M'

        actual = find_path(nodes_tuples, start, end)

        self.assertSequenceEqual(expected, actual)

    def test_count_occurrences_in_ordered_array(self):
        self.assertEqual(3, count_occurrences_ordered_array([1, 1, 1, 3], 1))
        self.assertEqual(4, count_occurrences_ordered_array([1, 1, 1, 1, 3], 1))
        self.assertEqual(1, count_occurrences_ordered_array([1, 1, 1, 1, 3], 3))
        self.assertEqual(1, count_occurrences_ordered_array([1, 1, 1, 3], 3))
        self.assertEqual(1, count_occurrences_ordered_array([0, 1, 1, 1], 0))

    def test_people_alive_in_years(self):
        people = [
            Person(1970, 1990),
            Person(2000, 2010),
            Person(2003, 2011),
            Person(1870, 1890),
            Person(1500, 1500),
            Person(1200, 1201),
            Person(2015, 2018),
            Person(1970, 2020),
            Person(2003, 2030),
        ]

        self.assertEqual((2003, 4), get_year_most_people_alive(people))

    def test_find_common_numbers_sorted_arrays(self):
        array1 = [1, 5, 8, 10, 12, 19, 33, 999]
        array2 = [0, 2, 3, 8, 10, 33, 34, 998, 999, 1000]

        expected = [8, 10, 33, 999]
        actual = find_common_integers_sorted_arrays(array1, array2)

        self.assertItemsEqual(expected, actual)

    def test_find_common_numbers_unsorted_arrays(self):
        array1 = [99, 320, 88, 76, 15, 0, 22]
        array2 = [0, 78, 22, 120, 2, 5, 7, 999, 88, 325]

        expected = [88, 0, 22]
        actual = find_common_integers_unsorted_arrays(array1, array2)

        self.assertItemsEqual(expected, actual)

    def test_are_brackets_balanced(self):
        balanced_brackets = '[{({}{}())}]'
        unbalanced_brackets_uneven = '[{)}]'
        unbalacend_brackets_even1 = '({[(]]})'
        unbalacend_brackets_even2 = '({[(()]})'

        self.assertTrue(check_if_brackets_are_balanced(balanced_brackets))
        self.assertFalse(check_if_brackets_are_balanced(unbalanced_brackets_uneven))
        self.assertFalse(check_if_brackets_are_balanced(unbalacend_brackets_even1))
        self.assertFalse(check_if_brackets_are_balanced(unbalacend_brackets_even2))

    def test_get_permutation_substrings(self):
        small_string = 'abc'
        big_string = 'aeroabcawpecbalwebcalqlcab'

        expected_perms = ['abc', 'cab', 'bca', 'cba']

        actual_perms = get_permutations_as_substring(small_string, big_string)

        self.assertItemsEqual(expected_perms, actual_perms)

    def test_task_queue(self):
        tasks = [1, 1, 2, 1]
        cooldown = 2

        expected_cycles = 7

        actual_cycles = count_cycles_for_task_queue(tasks, cooldown)

        self.assertEqual(actual_cycles, expected_cycles)

    def test_palindrome_removing_char(self):
        self.assertTrue(check_if_palindrome_removing_1_char('madam'))
        self.assertTrue(check_if_palindrome_removing_1_char('madabm'))
        self.assertTrue(check_if_palindrome_removing_1_char('mbadam'))
        self.assertTrue(check_if_palindrome_removing_1_char('maddabm'))
        self.assertTrue(check_if_palindrome_removing_1_char('mbaddam'))
        self.assertFalse(check_if_palindrome_removing_1_char('abc'))
        self.assertTrue(check_if_palindrome_removing_1_char('madbam'))
        self.assertTrue(check_if_palindrome_removing_1_char('mabdam'))
        self.assertFalse(check_if_palindrome_removing_1_char('mzadaxm'))
        self.assertFalse(check_if_palindrome_removing_1_char('xovos'))

    def test_average_on_binary_tree_levels(self):
        root = TreeNode(4)

        first_left = TreeNode(7)
        first_right = TreeNode(9)
        root.left = first_left
        root.right = first_right

        second_left_left = TreeNode(10)
        second_left_right = TreeNode(2)
        second_right_right = TreeNode(6)

        first_left.left = second_left_left
        first_left.right = second_left_right
        first_right.right = second_right_right

        third_right = TreeNode(6)
        second_left_right.right = third_right

        third_right.left = TreeNode(2)

        actual = find_average_amount_on_binary_tree_levels(root)
        expected = [4, 8, 6, 6, 2]

        self.assertEqual(expected, actual, 'average array per level does not match')

    def test_find_positions_of_max_element(self):
        numbers = [10, 9, 20, 5, 20, 8, 20]
        possible_results = [2, 4, 6]

        actual = find_position_of_max_element(numbers)
        self.assertIn(actual, possible_results)

    def test_min_heap(self):
        heap = Heap()

        heap.insert(99)
        heap.insert(80)
        heap.insert(10)

        heap.insert(5)

        self.assertSequenceEqual(heap.items, [5, 10, 80, 99])

        heap.extract_min()

        self.assertEqual(heap.items, [10, 99, 80])

    def test_number_of_meeting_rooms(self):
        meetings = [Meeting(0, 30), Meeting(5, 10), Meeting(15, 20)]

        rooms = get_number_of_rooms_needed(meetings)

        self.assertEqual(2, rooms)

    def test_largest_int_one_swap(self):
        expected = 54321
        actual = get_largest_int_with_one_swap(52341)
        self.assertEqual(expected, actual)

        expected = 993
        actual = get_largest_int_with_one_swap(993)
        self.assertEqual(expected, actual)