def linear_search(target, nums):
  for i in range(len(nums)):
    if nums[i] == target:
      return i
  return -1

def linear_search_comparisons(target, nums):
  comparisons = 0
  for i in range(len(nums)):
    comparisons += 1
    if nums[i] == target:
      return i, comparisons
    #that return creates a tuple -> so the return data type is a tuplex
  return -1

def binary_search(target, nums):
    lo, hi = 0, len(nums)-1

    while lo <= hi:
      mid = (lo + hi) // 2
      if nums[mid] < target:
        lo = mid + 1
      elif target < nums[mid]:
        hi = mid - 1
      else:
        return mid
      
    return -1

def binary_search_comparisons(target, nums):
    lo, hi = 0, len(nums)-1
    comparisons = 0

    while lo <= hi:
      comparisons += 1
      mid = (lo + hi) // 2
      if nums[mid] < target:
        lo = mid + 1
      elif target < nums[mid]:
        hi = mid - 1
      else:
        return mid, comparisons
    return -1, comparisons

if __name__ == "__main__":
  nums = [10*x for x in range(1024)]

  nums = [1,3,5,6,7,8,8,9,11,12,13,14,18,20]
  print("worksheet ans on line below:")
  print(binary_search(7,nums))

  print(linear_search(20, nums))
  print(binary_search(20, nums))

  
  #Tracking number of comparisons
  min, max = 1024, 0
  min_index, max_index = [], []
  
  for i in nums:
    index, comparisons = binary_search_comparisons(i, nums)
    if comparisons < min:
      min=comparisons
      min_index = index
    if comparisons > max:
      max=comparisons
      max_index = index

    #print(i, index, comparisons)

  print(f"min comparisons: {min} for index {min_index}")
  print(f"max comparisons: {max} for index {max_index}")
  
  