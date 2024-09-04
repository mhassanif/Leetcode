# :type nums: List[int]
# :rtype: None Do not return anything, modify nums in-place instead.

class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        while 0 in nums:
            nums.remove(0)  # Remove the first occurrence of 0
            count += 1  # Increment the count
        nums.extend([0] * count)
        