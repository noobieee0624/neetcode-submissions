class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        at 10 -> we make a negative profit, but this is our current
        cheapest option c.

        remember that if th eprices monotonically decrease, we can choose not to sell
        and make a profit of 0

        c = 10, [1, len-1]
        next iteraiton: min(c, prices[1]) -> c = 1
        keep track of the largest number we have now

        idea is to keep track of the smallest possible and largest possible values at 
        each iteration, because it gives us the maximum difference

        each loop, we keep the smallest and the largest number. at the end, return the 
        difference, and if smallest >= largest number, return 0

        but we run into the problem that a larger in and larger max can result in a 
        better difference

        we can either buy, or not buy--sell, or not sell:
        at i = 0: we keep track of buying it, and also selling it
        gives us two options: buy, sell = 0 and 
        '''
        buy = prices[0]
        profit = 0

        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p-buy)
        return profit
        
