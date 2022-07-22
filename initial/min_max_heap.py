
# list = [1, 2, 3, 4, 5, 6]
# list2 = [3, 23, 24, 6, 86, 87, 90]
# list3 = [2, 7, 8, 9, 23, 90, 93, 382, 2, 3, 89]
# list4 = [3, 6, 7]

# print(f'not heapified: {list2}')
#
# print(f'heapified: {list2}')
# heapq._heapify_max(list2)
# print(f'max_heap: {list2}')


def max_heap(array):
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        heapify_max(array, i)
    # return print(f'max: {array[0]}')
    return array[0]


def min_heap(array):
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        heapify_min(array, i)
    # return print(f'min: {array[0]}')
    return array[0]


def heapify_max(arr, i):
    n = len(arr)
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        # arr[i], arr[largest] = arr[largest], arr[i]  # swap
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp

        # Heapify the root.
        # print(arr)
        heapify_max(arr, largest)


def heapify_min(arr, i):
    n = len(arr)
    smallest = i  # Initialize lsmallestargest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] > arr[l]:
        smallest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[smallest] > arr[r]:
        smallest = r

    # Change root, if needed
    if smallest != i:
        # arr[i], arr[smallest] = arr[smallest], arr[i]  # swap
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp

        # Heapify the root.
        # print(arr)
        heapify_min(arr, smallest)


# def heapSort(arr):
#     n = len(arr)

#     # Build a maxheap.
#     for i in range(n//2 - 1, -1, -1):
#         print(f'n: {n}' + f' i: {i}')
#         heapify(arr, n, i)
#     print(list2)

#     # One by one extract elements
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # swap
#         heapify(arr, i, 0)


# max_heap(list)
# min_heap(list)
