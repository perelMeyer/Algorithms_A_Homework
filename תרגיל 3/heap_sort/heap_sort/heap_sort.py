# סעיף 3

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

# סעיף 4

def is_max_heap(arr, i=0, key=lambda x: x):
    for child in range(i + 1, len(arr)):
        p = parent(child)
        if key(arr[p]) < key(arr[child]):
            return False
    return True

# סעיף 5

def max_heapify(arr, i, heap_size, key=lambda x: x):
    largest = i
    l = left(i)
    r = right(i)

    # בדיקה מול הבן השמאלי
    if l < heap_size and key(arr[l]) > key(arr[largest]):
        largest = l

    # בדיקה מול הבן הימני
    if r < heap_size and key(arr[r]) > key(arr[largest]):
        largest = r

    # אם אחד הילדים גדול מהשורש — צריך להחליף ולרדת למטה
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key)

# סעיף 6

def build_max_heap(arr, key=lambda x: x):
    heap_size = len(arr)

    # Start from the last internal node and go upward
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(arr, i, heap_size, key)

# סעיף 7

def heap_sort(arr, key=lambda x: x):
    # Step 1: build max heap
    build_max_heap(arr, key)
    heap_size = len(arr)

    # Step 2: repeatedly extract max
    for i in range(heap_size - 1, 0, -1):
        # swap max (arr[0]) with last element
        arr[0], arr[i] = arr[i], arr[0]

        # reduce heap size
        heap_size -= 1

        # fix heap from the root
        max_heapify(arr, 0, heap_size, key)


if __name__ == "__main__":
    arr = [50, 30, 20, 15, 10, 8, 16]
    
    print("Array:", arr)

    if is_max_heap(arr):
        print("This is a valid MAX-HEAP")
    else:
        print("This is NOT a MAX-HEAP")

    arr1 = [20, 30, 50, 15, 10, 8, 16]

    print("Before max_heapify:", arr1)

    max_heapify(arr1, 0, len(arr1))

    print("After max_heapify:", arr1)

    arr3 = [3, 9, 2, 1, 4, 5]

    print("Before build_max_heap:", arr3)

    build_max_heap(arr3)

    print("After build_max_heap:", arr3)

    arr4 = [3, 9, 2, 1, 4, 5]

    print("Before heap_sort:", arr4)

    heap_sort(arr4)

    print("After heap_sort:", arr4)
