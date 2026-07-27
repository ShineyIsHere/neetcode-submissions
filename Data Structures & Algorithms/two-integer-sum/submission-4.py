class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        found = False
        for i in range(len(nums)):
            for j in dict:
                if dict[j] == nums[i]:
                    return [j, i]
            dict[i] = target - nums[i]
        return