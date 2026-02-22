import heapq

def merge_sorted_lists(lists, key):
    heap = []
    result = []

    # אתחול ההיפ: הכנסה של האיבר הראשון מכל רשימה
    for i, lst in enumerate(lists):
        if lst:  # הרשימה לא ריקה
            heapq.heappush(heap, (key(lst[0]), i, 0, lst[0]))

    # שליפה מהמינ-היפ והכנסת האיבר הבא מאותה רשימה
    while heap:
        _, list_index, element_index, value = heapq.heappop(heap)
        result.append(value)

        # אם יש איבר נוסף באותה רשימה — הכנס אותו להיפ
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(heap, (key(next_value), list_index, element_index + 1, next_value))

    return result

def key_func(x):
    return x

def main():
    lists = [
        [1, 4, 9],
        [2, 3, 10],
        [0, 7, 8]
    ]

    merged = merge_sorted_lists(lists, key_func)
    print("Merged list:", merged)


if __name__ == "__main__":
    main()
