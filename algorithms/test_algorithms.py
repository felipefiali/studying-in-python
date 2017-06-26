from unittest import TestCase
from algorithms.binary_search import *
from algorithms.find_numbers_that_sum import *
from algorithms.cake_eating_problem import *
from algorithms.heap_sort import *
from algorithms.merge_ordered_arrays import *
from algorithms.christmas_tree import *
from data_structures.queue_with_stacks import *
from data_structures.trie import *
from data_structures.lru import LRUCache
from algorithms.shortest_substring_with_strings import *
from algorithms.longest_increasing_sub_array import *
from algorithms.biggest_number_possible import *
from algorithms.next_bigger_number import *
from algorithms.string_edit_distance import *
from algorithms.longest_substring_unique_characters import *



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

    def test_heap_sort(self):
        self.assertSequenceEqual(heap_sort([5, 8, 1, 2, 5, 9, 0]), [0, 1, 2, 5, 5, 8, 9])
        self.assertSequenceEqual(heap_sort([5]), [5])
        self.assertSequenceEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertSequenceEqual(heap_sort([]), [])

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
        self.assertEqual(6, get_edit_distance('esse aqui eh um exemplo', 'esse aqui é outro exemplo'))

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





