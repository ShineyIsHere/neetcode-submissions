class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max = 1
        count = 0
        current_substring = []
        for i in range(len(s)):
            if s[i] not in current_substring:
                current_substring.append(s[i])
                count += 1
                if count >= max:
                    max = count
            else:
                if count >= max:
                    max = count
                idx = current_substring.index(s[i])
                current_substring = current_substring[idx+1:]
                current_substring.append(s[i])
                count = len(current_substring)
        return max