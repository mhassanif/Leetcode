class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=1
        count=1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                # prev element not same
                count=1 # new element first occurence
            else:
                # its the same element again
                count+=1
            
            if count<=2:
                nums[slow]=nums[i]
                slow+=1
        return slow

