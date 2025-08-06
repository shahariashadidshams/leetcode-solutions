class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    i = 0
    for num in nums:          # scan once
      if num != val:          # keep anything ≠ val
        nums[i] = num         # overwrite in-place
        i += 1
    return i                  # i == k, the count of kept elements


print(Solution().removeElement([3, 2, 2, 3], 3))
print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(Solution().removeElement([], 0))