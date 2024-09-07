class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        avg = 0
        #calculate initial avg
        for i in range(k):
            avg += nums[i]/float(k)
        # set initial avg as max
        max_avg = avg
        prev = 0
        next = k
        #sliding window running avg 
        # removes prev adds next
        while next<len(nums):
            avg += nums[next]/float(k)
            avg -= nums[prev]/float(k)
            prev+=1
            next+=1
            if avg>max_avg:
                max_avg = avg
        return max_avg
        