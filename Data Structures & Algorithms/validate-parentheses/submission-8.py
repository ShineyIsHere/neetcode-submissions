class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif len(stack) == 0:
                continue
            elif abs(ord(i) - ord(stack[-1])) > 2:
                return False
            else:
                stack.pop()
        return True
            