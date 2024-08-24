class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the value and its index
        num_dict = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # If the complement is already in the dictionary, return its index and the current index
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Otherwise, add the current number to the dictionary with its index
            num_dict[num] = i
