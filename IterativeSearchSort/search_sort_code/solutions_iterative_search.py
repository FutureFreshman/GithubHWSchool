# Problem 5
def is_duplicate(target: int | float, nums: list) -> bool:
    '''Determines whether a given number exists more than
    once in a list of unsorted numbers

    Args:
      target (int or float): The number to search for
      nums (list): A list of numbers
    
    Returns:
      bool - True if n is duplicated, false otherwise
    '''
    count = 0
    for num in nums: # Iterate through each number in list
        if num == target: # Check if the number is our target
            count += 1 # Increase the count
            if count == 2:
                # If we've seen the number twice, it's a duplicate -> immediately return True
                return True
    
    # Finished loop without finding duplicates - return False
    return False

# Problem 6
def count_n(target: int | float, nums: list) -> int:
    '''Determines how many times a given number is present
    in a list of unsorted numbers

    Args:
      target (int or float): The number to search for
      nums (list): A list of numbers
    
    Returns:
      int - Number of times target appears in the list
    '''
    count = 0 # Start count at 0
    for num in nums: # Iterate through each number in list
        if num == target: # Check if the number is our target
            count += 1 # Increase the count
    
    # Now that we've finished iterating through the list, return the count
    return count

# Problem 7
def find_max(nums: list) -> int | float:
    '''Finds the maximum value in an unsorted list of numbers

    Args:
      nums (list): A list of numbers
    
    Returns:
      int or float - The largest number in the list
    '''
    # Create a running max and set it to the first element in the list
    # NOTE: Avoids setting to 0 (or another constant) - list could be all negative!
    current_max = nums[0]

    for num in nums[1:]: # Iterate through each subsequent number in list
        if num > current_max:
            # If the current number is the largest we've seen so far, update current_max
            current_max = num
    
    # Return current_max, which will be the largest number in the list since we've now iterated through
    # the whole thing
    return current_max

# Problem 8 - Brute Force Solution
def max_sum(nums) -> int | float:
    '''Finds the maximum sum that can be made from adding any two numbers
    in a list of unsorted numbers

    Args:
      nums (list): A list of numbers
    
    Returns:
      int or float - The largest sum that can be made from adding 2 numbers in the list
    '''
    # NOTE: We need to make sure to not pair up numbers with the same index. We could do this using
    # the approach below, or by starting the second range() at i + 1, which would also avoid duplicate
    # comparisons.

    # Set the current maximum sum to the sum of the first two numbers
    # NOTE: Avoids the same problem discussed in find_max()
    current_max_sum = nums[0] + nums[1]
    
    # Iterate over every possible pair of indices
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j: # Prevents summing an element with itself
                if (nums[i] + nums[j] > current_max_sum) and (i != j):
                    # If the sum of these two elements is greater than the maximum, 
                    current_max_sum = nums[i] + nums[j]
    
    return current_max_sum


            
print(is_duplicate(3, [1, 2, 3, 4, 5, 3])) # True
print(is_duplicate(6, [1, 2, 3, 4, 5]))    # False
print(count_n(3, [3, 2, 3, 4, 3, 5, 3]))   # 4
print(count_n(6, [1, 2, 3, 4, 5]))         # 0
print(find_max([1, 3, 2, 5, 4]))           # 5
print(find_max([-1, -3, -20, -5]))         # -1
print(max_sum([1, 2, 3, 4, 5]))            # 9
print(max_sum([-10, -3, -20, -5]))         # -8