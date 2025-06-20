def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i

        # Iterate through the unsorted portion (from i+1 to the end)
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        
        if min_idx != i: # This check makes it slightly more efficient if element is already in place
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
