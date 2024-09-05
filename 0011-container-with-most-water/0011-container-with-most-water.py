class Solution:
    def maxArea(self, height):
        left = 0           
        right = len(height) - 1  
        maxWater = 0        
        
        while left < right:
            # width & height
            width = right - left
            h = min(height[left], height[right])
            
            # Calculate water 
            water = width * h
            
            # Update maximum 
            maxWater = max(maxWater, water)
            
            # smaller side moves in
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater