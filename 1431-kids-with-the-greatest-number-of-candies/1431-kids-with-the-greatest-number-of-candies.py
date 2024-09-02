# :type candies: List[int]
# :type extraCandies: int
# :rtype: List[bool]

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        most = max(candies) 
        return [c + extraCandies >= most for c in candies]


# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         result = []
#         most =  max(candies)
#         for c in candies:
#             result.append(c+extraCandies>=most)
#         return result

