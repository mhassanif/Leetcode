# maps to previous problem
# lonest subarray of ones where u can flip k zeros
# APPORACH : we find the longest subarray of 1's allowing at max 1 zero
# ie that zero will be deleted
class Solution(object):
    def longestSubarray(self, nums):
        left = 0 
        maxDeletions = 1  # num of deletable elements
        for right in range(len(nums)):
            if nums[right]==0:
                maxDeletions-=1
            # maxDeletions -= 1 - nums[right]
            
            if maxDeletions < 0:
                # more than one zero
                if nums[left]==0:
                    maxDeletions+=1
                # maxDeletions += 1 - nums[left]
                left += 1
                # shrink from the left to keep at max 1 zero 
            # print(nums[left:right+1])

        return right - left

'''
EXPLAINATION 
- a while or a max variale too keep track is not used because : 
if we reach an invlaid subarray we try to shrink from left one index at a time
at the same time right index is constantly increaseing (for loop)

so even if the current subarray is invalid, the difference between left and right is the length of the max we found previously
(since right increases in the for loop and left is increasing to shrink)
if we are unable to shrink to a valid array and the right reaches end 

the right - left is the length of the longest we found previousy
if we are able to shrink and the right increaase without needing the left to shrink 
we have found a new longest
'''