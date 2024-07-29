def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # Misplaced final swap
        if i == n-1:
            arr[0], arr[-1] = arr[-1], arr[0]
    return arr
