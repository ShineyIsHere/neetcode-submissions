class Solution:
    def Counting(self, n):
        count = 0
        for i in range(32):
            if n & ( 1 << i) != 0:
                count += 1
        return count
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            val = self.Counting(i)
            output.append(val)
        return output