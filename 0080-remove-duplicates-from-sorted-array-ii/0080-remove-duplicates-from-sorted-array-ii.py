class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=1
        count=1
        for fast in range(1,len(nums)):
            if nums[fast-1]!=nums[fast]:
                count=1
            else:
                count+=1
            if count<=2:
                nums[slow]=nums[fast]
                slow+=1
        return slow
