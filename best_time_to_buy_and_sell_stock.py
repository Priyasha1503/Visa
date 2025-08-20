
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''buy=float('inf')
        max_profit=0
        for i in range(0,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            else:
                #sold_max=max(sold_max,prices[i])
                sold=prices[i] 
                max_profit=max(max_profit,sold-buy)
        return max_profit'''

        ###REVISION
        cp=float('inf')#cost price - the price which we are buying
        sp=0#selling price - the proce which we are selling it for
        maxprofit=0
        for i in range(0,len(prices)):
            if cp>prices[i]:
                cp=prices[i]
                sp=0 # u can write this step for making sure the sp=0,so, that the max will be compared - the below step - max(sp,prices[i])
            else:
                sp=max(sp,prices[i]) #
                maxprofit=max(maxprofit,abs(cp-sp))
        return maxprofit

 
