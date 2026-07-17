class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp1 = "".join(sorted(s))
        tmp2 = "".join(sorted(t))
        if tmp1 == tmp2:
            return True
        else:
            return False