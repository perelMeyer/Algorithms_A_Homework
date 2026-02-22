def partition_hoare(a, key):
    pivot = key(a[0])           # pivot הוא האיבר הראשון
    i = -1
    j = len(a)

    while True:
        # זזים ימינה עד שמוצאים איבר >= pivot
        i += 1
        while key(a[i]) < pivot:
            i += 1

        # זזים שמאלה עד שמוצאים איבר <= pivot
        j -= 1
        while key(a[j]) > pivot:
            j -= 1

        if i >= j:
            return j            # נקודת החיתוך

        a[i], a[j] = a[j], a[i]

def main():
    # Example list
    arr1 = [7, 2, 9, 4, 3, 8]
    arr2 = arr1.copy()

    print("Original list:", arr1)

    # Hoare
    idx_hoare = partition_hoare(arr2, key=lambda x: x)
    print("\n--- Hoare ---")
    print("After partition:", arr2)
    print("Cut index:", idx_hoare)


if __name__ == "__main__":
    main()

