class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = []
        for i in nums:
            if i in val:
                return True
            else:
                val.append(i)
        return False