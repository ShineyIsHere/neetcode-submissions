class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = []
        if len(prices) == 1:
            return 0
        for i in range(len(prices)):
            if i == 0:
                continue
            val = prices[i] - min(prices[0:i])
            output.append(val)
        if max(output) < 0:
            return 0
        return max(output)
