def bubble_sort(unsorted_list):
    arr = list(unsorted_list)
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
            
    return arr
