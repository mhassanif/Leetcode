class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        - non-val is copied and k moves
        - if its val k doesn't move ie stays at position of val
        - when i meets a non val it copies that to postion where val was
        - hence val gets overwritten
        - since k stopped eveytime it met a val
        - it only moved forward only non val times
        - hence directly return k
        """
        k = 0 # copy position
        for i in range(len(nums)):
            if nums[i]==val:
                # copy non-val back 
                nums[k]=nums[i]
                k+=1
        return k 