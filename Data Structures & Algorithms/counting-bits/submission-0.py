class Solution:
    def BinaryConvert(self, n):
        if n < 2:
            return n
        bi = 0
        flag = False
        idx = 1
        while n//2 != 0:
            if flag == True:
                n //= 2
            bi = bi + n%2 * idx
            flag = True
            idx *= 10
        return bi
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