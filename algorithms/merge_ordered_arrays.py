def merge_ordered_arrays(list_of_arrays):
    numbers_to_arrays_indices = {}
    arrays_index_position = {}

    for array_index, array in enumerate(list_of_arrays):
        first_item_in_array = array[0]

        if first_item_in_array not in numbers_to_arrays_indices:
            numbers_to_arrays_indices[first_item_in_array] = []

        numbers_to_arrays_indices[first_item_in_array].append(array_index)
        arrays_index_position[array_index] = 0

    temp_heap = [array[0] for array in list_of_arrays]

    sorted_array = []

    make_min_heap(temp_heap, len(temp_heap) - 1)

    while len(temp_heap) > 0:
        smallest_number = temp_heap.pop(0)

        array_index = numbers_to_arrays_indices[smallest_number].pop()

        arrays_index_position[array_index] += 1
        index_incremented = arrays_index_position[array_index]

        sorted_array.append(smallest_number)

        if len(list_of_arrays[array_index]) > index_incremented:
            number_to_be_added_to_heap = list_of_arrays[array_index][index_incremented]

            if number_to_be_added_to_heap not in numbers_to_arrays_indices:
                numbers_to_arrays_indices[number_to_be_added_to_heap] = []

            numbers_to_arrays_indices[number_to_be_added_to_heap].append(array_index)

            temp_heap.append(number_to_be_added_to_heap)

        make_min_heap(temp_heap, len(temp_heap) - 1)

    return sorted_array


def make_min_heap(array, heap_size):
    for i in range(heap_size // 2, -1, -1):
        heapify(array, i)


def heapify(heap, i):
    heap_size = len(heap) - 1

    left = 2 * i
    right = 2 * i + 1

    smallest = i

    if left <= heap_size and heap[left] < heap[smallest]:
        smallest = left

    if right <= heap_size and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        temp = heap[i]
        heap[i] = heap[smallest]
        heap[smallest] = temp

        heapify(heap, smallest)





