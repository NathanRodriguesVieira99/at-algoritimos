def bubble_sort(arr):
    arr = list(arr)
    n = len(arr)
    comparisons = 0
    copies = 0

    for i in range(n - 1):
        has_changed = False
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                copies += 3
                has_changed = True
        if not has_changed:
            break

    return arr, comparisons, copies


def selection_sort(arr):
    arr = list(arr)
    n = len(arr)
    comparisons = 0
    copies = 0

    for i in range(n - 1):
        lowest_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[lowest_index]:
                lowest_index = j
        if lowest_index != i:
            arr[i], arr[lowest_index] = arr[lowest_index], arr[i]
            copies += 3

    return arr, comparisons, copies


def insertion_sort(arr):
    arr = list(arr)
    n = len(arr)
    comparisons = 0
    copies = 0

    for i in range(1, n):
        key = arr[i]
        copies += 1
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                copies += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        copies += 1

    return arr, comparisons, copies


data = [5, 2, 4, 1, 3]

print(bubble_sort(data))
print(selection_sort(data))
print(insertion_sort(data))
print(data)
