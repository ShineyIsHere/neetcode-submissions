class Solution:
    def findMax(self, nums, l, r):
        return max(nums[l:r+1])
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        output = []
        while r <= len(nums) - 1:
            output.append(self.findMax(nums,l,r))
            l += 1
            r += 1
        return output