class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if i == 0:
                stack.append([i, temperatures[i]])
            elif len(stack) > 0 and temperatures[i] <= stack[-1][1]:    
                stack.append([i, temperatures[i]])
            else:
                while len(stack) > 0 and temperatures[i] > stack[-1][1]:
                    output[stack[-1][0]] = (i - stack[-1][0])
                    stack.pop()
                stack.append([i, temperatures[i]])
        return output 
            