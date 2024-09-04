# :type nums: List[int]
# :rtype: bool

class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')
    
        for num in nums:
            if num <= first:
                first = num  
            elif num <= second:
                # smaller than second but larger than first
                second = num  
            else:
                # num larger than first & second
                return True
        return False

    

# ALTERNATE SOLUTION  : O(N^2)

# def increasingTriplet(self, nums):
#     n = len(nums)
#     for i in range(1, n - 1):
#         left_smaller = any(nums[j] < nums[i] for j in range(i))
#         right_larger = any(nums[k] > nums[i] for k in range(i + 1, n))
        
#         if left_smaller and right_larger:
#             return True
#     return False