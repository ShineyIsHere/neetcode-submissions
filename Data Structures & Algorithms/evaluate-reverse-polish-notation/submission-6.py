class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        for i in tokens:
            if i not in ["+","-","*","/"]:
                i = int(i)
                stack.append(i)
            elif i == "+":
                val = (int(stack.pop(-1)) + int(stack.pop(-1)))
                stack.append(val)
            elif i == "-":
                val = (int(stack.pop(-2)) - int(stack.pop(-1)))
                stack.append(val)
            elif i == "*":
                val = (int(stack.pop(-1)) * int(stack.pop(-1)))
                stack.append(val)
            elif i == "/":
                val = int(stack.pop(-2)/stack.pop(-1))
                stack.append(val)
        return stack[-1]