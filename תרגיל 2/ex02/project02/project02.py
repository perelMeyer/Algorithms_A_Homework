from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def is_sorted(a, key=lambda x: x):
   # """
   # בודקת אם הרשימה a מסודרת בסדר עולה לפי פונקציית key.
   # מחזירה True אם מסודרת, אחרת False.
   # """
    # pairwise מחזירה זוגות עוקבים (x,y) מתוך הרש lista
    return all(key(x) <= key(y) for x, y in pairwise(a))


def merge(a, b, key=lambda x: x):
   # """
   # ממזגת שתי רשימות ממוינות בסדר עולה לפי key.
   # אם אחת הרשימות אינה ממוינת, הפונקציה מחזירה None.
   # """
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None

    i, j = 0, 0
    merged = []

    # מיזוג בסגנון merge של mergesort
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # הוספת שארית הרשימות
    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged

if __name__ == "__main__":

    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8]

    result = merge(a, b, key=lambda x: x)
    print(result)