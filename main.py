import random

# Úkol 1, vytvoření pole s 10 random číslama
array = [random.randint(0, 100) for _ in range(10)]
print("Původní pole:", array)

# Úkol 2, bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Úkol 3, bogo sort
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

# Úkol 4, selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Úkol 5, insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

# Vypsání výsledků 
print("Bubble sort:", bubble_sort(array.copy()))
print("Bogo sort:", bogo_sort(array.copy()))
print("Selection sort:", selection_sort(array.copy()))
print("Insertion sort:", insertion_sort(array.copy()))
