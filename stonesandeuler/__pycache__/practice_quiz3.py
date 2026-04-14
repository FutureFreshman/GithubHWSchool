def bubble_sort(arr):
    n = len(arr)                          # Get how many items are in the list
    for i in range(n):                    # Repeat n times (each pass moves one large item to the end)
        for j in range(0, n - i - 1):     # Go through the list up to the last unsorted element
            if arr[j] > arr[j + 1]:       # If the current item is bigger than the next one
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap them
    return arr                            # Return the sorted list

def insertion_sort(arr):
    for i in range(1, len(arr)):            # Start from the 2nd element (index 1)
        key = arr[i]                      # The element we want to insert into the sorted section
        j = i - 1                         # Look at the element just before key

        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:    
            arr[j + 1] = arr[j]           # Shift the element right
            j -= 1                        # Move one position left

        arr[j + 1] = key                  # Place key into the correct (open) spot
    return arr                            # Return the sorted list
