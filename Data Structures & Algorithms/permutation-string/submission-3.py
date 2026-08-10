class Solution:
    def isValid(self, s1, s2, l, r):
        tmp1 = "".join(sorted(s1))
        tmp2 = "".join(sorted(s2[l:r]))
        return True if tmp1 == tmp2 else False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        while r <= len(s2):
            output = self.isValid(s1,s2,l,r)
            if output == True:
                return True
            l += 1
            r += 1
        return False