def heap_sort(array):
    build_heap(array, len(array))

    heap_size = len(array) - 1

    for i in range(heap_size, -1, -1):
        temp = array[0]
        array[0] = array[heap_size]
        array[heap_size] = temp
        heap_size -= 1
        heapify(array, 0, heap_size)

    return array


def build_heap(array, size):
    heap_size = size - 1

    for i in range(heap_size // 2, -1, -1):
        heapify(array, i, heap_size)


def heapify(array, i, heap_size):
    left = 2 * i
    right = 2 * i + 1
    largest = i

    if left <= heap_size and array[left] > array[i]:
        largest = left

    if right <= heap_size and array[right] > array[largest]:
        largest = right

    if largest != i:
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp

        heapify(array, largest, heap_size)


