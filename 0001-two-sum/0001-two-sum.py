class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for i,num in enumerate(nums):
            need = target - num
            if need in visited:
                return [visited[need],i]
            visited[num]=i
