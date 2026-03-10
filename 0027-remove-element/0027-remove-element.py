class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx=[]
        for i in range(len(nums)):
            if nums[i]==val:
                idx.append(i)
        moved=0
        for i in range(len(idx)):
            nums.pop(idx[i]-moved)
            moved+=1
        return len(nums)