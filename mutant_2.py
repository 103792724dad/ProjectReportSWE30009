def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-2):  # Altered loop range
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
