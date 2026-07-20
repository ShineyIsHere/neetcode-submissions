class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i == j:
                    continue
                else:
                    val = min(heights[i], heights[j]) * abs(i - j)
                    if val > max_val:
                        max_val = val
        return max_val