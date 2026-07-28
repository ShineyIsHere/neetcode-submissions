class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0
        for i in range(32):
            if n & (1 << i):
                val += 2**(31-i)
        return val