# :type nums: List[int]
# :type k: int
# :rtype: int

class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zeroCount = 0
        maxLength = 0
        
        # Sliding window
        for right in range(len(nums)):
            # Add the current number to the window
            if nums[right] == 0:
                zeroCount += 1
            
            # Shrink the window if the number of zeros exceeds k
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1  # Move the left pointer to shrink the window
            # Calculate the maximum length of valid subarray
            maxLength = max(maxLength, right - left + 1)
            print(nums[left:right+1])
            print(right - left + 1)
        
        return maxLength

# (right - left + 1) is actully current number of consecutive ones since only flipable number of zeros is inculeded & rest are already one

'''
Explanation:
    - left pointer is used to track the start of the window, and right is used to expand the window
    - We increment the right pointer through the array, expanding the window.
    - If we encounter more than k zeros, we move the left pointer (shrink the window) until the number of zeros is within the limit.
    - The variable maxLength keeps track of the maximum length of a valid subarray (where the number of flipped 0s is ≤ k).
'''


        

        

        