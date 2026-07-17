class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        val = []
        count = 0
        for i in range(len(nums)):
            if i == 0:
                count += 1
                continue
            elif nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]:
                if i == len(nums) - 1:
                    count += 1
                    val.append(count)
                else:
                    continue
            else:
                val.append(count)
                count = 1
        val.append(count)
        val.sort()
        return val[len(val) - 1]
                