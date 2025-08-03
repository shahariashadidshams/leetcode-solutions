def moveZeroes(nums: list[int]):
    a = 0                     
    for num in nums:
      if num != 0:
        nums[a] = num
        a += 1
    for b in range(a, len(nums)):
      nums[b] = 0

nums = [0, 6, 0, 3, 5, 0, 1, 3, 4, 10, 99, 0, 22, 33, 0, 100]
moveZeroes(nums)
print(nums)

"""
Move Zeroes:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.
"""