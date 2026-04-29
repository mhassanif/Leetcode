class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            running=cur_sum+nums[i]
            cur_sum = max(running,nums[i])
            max_sum = max(max_sum,cur_sum)
        return max_sum