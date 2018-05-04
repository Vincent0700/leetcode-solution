class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        x = len(prices)
        if(x == 0):
            return 0
        elif(x == 1):
            return 0
        elif(x == 2):
            p = prices[1] - prices[0]
            return p if p > 0 else 0

        left = prices[0:x/2]
        right = prices[x/2:]
        leftProfit = self.maxProfit(left)
        rightProfit = self.maxProfit(right)
        midProfit = max(right) - min(left)
        p = max(leftProfit, rightProfit, midProfit)
        return p if p > 0 else 0


print Solution().maxProfit([2, 1])
