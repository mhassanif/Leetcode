class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf') # infinite minimum
        max_profit = 0 # 0 max profit 

        for price in prices:
            min_price = min(min_price,price) # min price so far
            profit = price - min_price # current profit if sell today
            max_profit = max(max_profit,profit) # update profit if bigger
        
        return max_profit