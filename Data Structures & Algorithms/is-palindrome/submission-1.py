class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if i.isalpha() == False and i.isnumeric() == False:
                s = s.replace(i, "")
        s = s.lower()
        t = "".join(reversed(s))
        if s == t:
            return True
        else:
            return False

            