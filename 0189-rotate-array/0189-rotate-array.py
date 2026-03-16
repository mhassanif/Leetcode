class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # slicing method

        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k] 

        # reverse method
        n = len(nums)
        k = k % n
        
        def reverse(l,r):
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
                
        reverse(0,n-1) # reverse whole aray
        reverse(0,k-1) # reverse first k 
        reverse(k,n-1) # reverse remaning
        