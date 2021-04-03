def pipe_fix(nums):
  
    nums = sorted(nums, key = None)
    minimum = nums[0]
    maximum = nums[-1] + 1

    solution = []
    for number in range(minimum, maximum):
        solution.append(number)
  
  return solution