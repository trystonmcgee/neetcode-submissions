class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        maxx = 0

        for num in prices:
            if num < min_price:
                min_price = num

            curr = num - min_price
            if curr > 0 and curr > maxx:
                maxx = curr

        return maxx                   
