def partition_lomuto(a, key):
    pivot = key(a[-1])          # pivot הוא האיבר האחרון
    i = -1                      # גבול האזור של "קטנים מה-pivot"

    for j in range(len(a) - 1):
        if key(a[j]) <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    # מעבירים את ה-pivot למקום הנכון
    a[i + 1], a[-1] = a[-1], a[i + 1]
    return i + 1

def main():
    # Example list
    arr1 = [7, 2, 9, 4, 3, 8]
    arr2 = arr1.copy()

    print("Original list:", arr1)

    # Lomuto
    idx_lomuto = partition_lomuto(arr1, key=lambda x: x)
    print("\n--- Lomuto ---")
    print("After partition:", arr1)
    print("Pivot index:", idx_lomuto)

if __name__ == "__main__":
    main()


