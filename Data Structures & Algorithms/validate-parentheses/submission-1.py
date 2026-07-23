class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        flag = False
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif len(stack) == 0:
                continue
            elif ord(i) - ord(stack[-1]) > 2 or ord(i) - ord(stack[-1]) < 0:
                return False
            else:
                stack.pop()
                flag =True
        if flag == False or len(stack) != 0:
            return False
        return True
            