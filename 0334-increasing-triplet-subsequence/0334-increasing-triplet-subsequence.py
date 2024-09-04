# # :type nums: List[int]
# # :rtype: bool

# class Solution(object):
#     def increasingTriplet(self, nums):
#         # initialize with infinity
#         first = second = third = float('inf') 
#         second_i = len(nums)-1
#         for n in nums: 
#             # when updating ensure first isnt updated to index greater than second
#             if n <= first : 
#                 first = n
#             elif n <= second:
#                 second = n
#                 second_i = nums.index(second)
#             elif n <= third:
#                 third = n
#                 print(first,second,third)
#                 return True
#         return False


