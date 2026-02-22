def quick_kth(arr, left, right, k, key=lambda x: x):
    
    # מחזירה את האיבר ה-k בגודל לפי key, מתוך arr[left:right+1]
    # k הוא אינדקס יחסי: 0 אומר "האיבר הקטן ביותר"
   

    if left == right:
        return arr[left]

    # חלוקה בסגנון לומוטו
    def partition(arr, left, right, key):
        pivot = key(arr[right])
        i = left
        for j in range(left, right):
            if key(arr[j]) <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    pivot_index = partition(arr, left, right, key)

    # כמה איברים יש בצד שמאל של הפיבוט
    left_size = pivot_index - left

    if k == left_size:
        return arr[pivot_index]
    elif k < left_size:
        return quick_kth(arr, left, pivot_index - 1, k, key)
    else:
        return quick_kth(arr, pivot_index + 1, right, k - left_size - 1, key)

def main():
    students = [
        ("Dana", 87),
        ("Avi", 92),
        ("Noa", 75),
        ("Rina", 90)
    ]

    # מוצא את הסטודנט עם הציון הכי נמוך
    result = quick_kth(students, 0, len(students)-1, 0, key=lambda x: x[1])
    print("The chosen student:", result)

main()
