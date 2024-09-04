# # :type nums: List[int]
# # :rtype: None Do not return anything, modify nums in-place instead.

class Solution(object):
    def moveZeroes(self, nums):
        non_zero = 0  # Pointer for non-zero elements
        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                # swap
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
        

# ALTERNATE APPROACH   

# class Solution(object):
#     def moveZeroes(self, nums):
#         count = 0
#         while 0 in nums:
#             nums.remove(0)  # Remove the first occurrence of 0
#             count += 1  # Increment the count
#         nums.extend([0] * count)