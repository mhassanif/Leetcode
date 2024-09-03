# :type nums: List[int]
# :rtype: List[int]

#  prouct without self : 
#       product to the left of i * product to the right of i

class Solution(object):
    def productExceptSelf(self, nums):

        length = len(nums)

        #initialized with 1's
        result = [1] * length
        
        # Compute left products
        left_product = 1
        for i in range(length):
            result[i] = left_product
            #assign & update left prod for next
            left_product *= nums[i]
        
        # Compute right products and finalize the result
        right_product = 1
        #iterate backward (same concept as left product)
        for i in range(length - 1, -1, -1):
            result[i] *= right_product
            # assign and update right prod for next
            right_product *= nums[i]
        
        return result
