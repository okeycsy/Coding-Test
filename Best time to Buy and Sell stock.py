import sys

class Solution:
    def sol(self,prices:list)->int:
        min_price = sys.maxsize
        profit=0

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)

        return profit