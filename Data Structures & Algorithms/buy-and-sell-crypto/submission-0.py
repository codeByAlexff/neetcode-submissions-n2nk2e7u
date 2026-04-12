class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Two Pointer
        buy , sell = 0,1

        #Initialize max profit
        maxP = 0

        #while sell less than length of prices
        while sell < len(prices):

            #if sell more than buy
            if prices[sell] > prices[buy]:
                #profit is sell - buy
                profit = prices[sell] - prices[buy]
                #update max profit to be
                #return the max between profit and maxP
                maxP = max(profit, maxP)
            #Check if buy = sell
            else:
                buy = sell
            #Add one more day to sell
            sell += 1
        return maxP
        