class Solution:
    def FindMostCommonElement(self, s):
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        val = 0
        for i in dict:
            if dict[i] >= val:
                val = dict[i]
        return val
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        count = 0
        max = 1
        left = 0
        right = 1
        while right <= len(s):
            if len(s[left:right]) - self.FindMostCommonElement(s[left:right]) <= k:
                right += 1
                count += 1
                if count > max:
                    max = count
            else:
                left += 1
                count -= 1
                if count > max:
                    max = count
        return max

