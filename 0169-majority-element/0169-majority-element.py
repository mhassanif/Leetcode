from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method 1:
        # return Counter(nums).most_common(1)[0][0]
        
        # method 2:
        freq={}
        for num in nums:
            freq[num]= freq.get(num,0)+1

        majority=nums[0]
        majoritycount=freq[nums[0]]
        # for num in nums:
        #     if freq[num]>majoritycount:
        #         majoritycount=freq[num]
        #         majority=num
        # return majority
        return max(freq, key=lambda x: freq[x])

        