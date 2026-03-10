class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx=[]
        # mark the positons
        for i in range(len(nums)):
            if nums[i]==val:
                idx.append(i)
        left_shift=0
        # pop the postions considering shift
        for i in range(len(idx)):
            nums.pop(idx[i]-left_shift)
            left_shift+=1
        return len(nums)