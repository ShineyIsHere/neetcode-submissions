class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        val = 0
        while L < R:
            tmp = min(heights[L], heights[R]) * (R - L)
            if tmp > val:
                val = tmp
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return val