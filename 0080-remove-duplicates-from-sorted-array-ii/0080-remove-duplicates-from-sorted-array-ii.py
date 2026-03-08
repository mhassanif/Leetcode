class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=1 # keep track of where to write 
        count=1
        for fast in range(1,len(nums)):
            # count tracking
            if nums[fast]!=nums[fast-1]:
                # new number - reset count
                count=1
            else:
                # old number - increment count
                count+=1
            
            # write or not
            if count<=2:
                # number came first or second time max
                # only happens after count reset 
                nums[slow]=nums[fast]
                slow+=1
        return slow


