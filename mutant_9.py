def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j], arr[j+1]  # Correct but with an extra swap
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr
