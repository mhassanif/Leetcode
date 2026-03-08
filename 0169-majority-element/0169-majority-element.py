from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]
        # freq = {}
        # for x in nums:
        #     freq[x] = freq.get(x,0)+1
        
        # max_count = 0
        # majority = nums[0]
        # for num in freq:
        #     if freq[num] > max_count:
        #         max_count = freq[num]
        #         majority = num
        # return majority