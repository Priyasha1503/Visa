#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp=float('inf')
        sp=0
        maxprofit=0
        for i in range(0,len(prices)):
            if i!=len(prices)-1:
                if prices[i]<prices[i+1]:
                    cp=prices[i]
                    sp=prices[i+1]
                    profit=abs(cp-sp)
                    print(i,i+1)
                    maxprofit+=profit
        return maxprofit


        
