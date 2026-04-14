def selection_sort(nums: list) -> None:
    '''Sorts a list using the selection sort algorithm

    Args:
      nums (list): A list of numbers
    '''
    # Iterate through each index from start to 2nd-to-last
    for i in range(len(nums) - 1):
        # Find the minimum element in the rest of the array
        # Start by setting idx_min to the current index
        idx_min = i
        # Iterate through all the subsequent elements to find the minimum
        for j in range(i + 1, len(nums)):
            if nums[idx_min] > nums[j]:
                # If we find an element that's smaller than what we've seen so far, update idx_min
                idx_min = j

        # Swap the minimum in the remaining list with the current index
        nums[i], nums[idx_min] = nums[idx_min], nums[i]

def insertion_sort(nums) -> None:
    '''Sorts a list using the insertion sort algorithm

    Args:
      nums (list): A list of numbers
    '''
    #comment 1:
    for i in range(1, len(nums)):
        #comment 2:
        current = nums[i]
        #comment 3:
        j = i - 1
        #comment 4:         
        while j >= 0 and current < nums[j]: 
                #comment 5:
                nums[j+1] = nums[j]
                #comment 6:
                j -= 1
        #comment 7:
        nums[j+1] = current


if __name__ == "__main__":
    #nums = [1, 10, 2, 3, 9, 8, 3, 4, 6, 2, -1, -8, 5, 7]
    #sortedList = [-8, -1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    #reverseSortedList =[10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1, -1, -8]
    #manyDuplicatesList =[9, 9, 5, 9, 9, 5, 5, 2, 9, 2, 2, 5, 9, 5]
    ws = [8,6,4,-2,0,4]
    print(ws)
    insertion_sort(ws)
    print(ws)
    