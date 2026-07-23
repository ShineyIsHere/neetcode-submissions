class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            tmp = ""
            return tmp
        tmp = ""
        length = ""
        for n in strs:
            length = str(len(n))
            tmp += length + "#" + n
        return tmp
    def decode(self, s: str) -> List[str]:
        output = []
        if len(s) == 0:
            return output
        length = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                length = length * 10 + int(s[i])
                i += 1
                continue
            print(length)
            tmp = ""
            tmp = s[i + 1:i + 1 + length]
            output.append(tmp)
            i = length + 1 + i
            length = 0
        return output
        return output