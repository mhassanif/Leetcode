from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for num in nums:
            freq[num]= freq.get(num,0)+1

        majority=nums[0]
        majoritycount=freq[nums[0]]
        for num in nums:
            if freq[num]>majoritycount:
                majoritycount=freq[num]
                majority=num
        return majority
        