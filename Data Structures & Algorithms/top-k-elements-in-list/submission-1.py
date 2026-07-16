class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        output = []
        for i in nums:
            found = False
            for j in dict:
                if i == j:
                    dict[j] += 1
                    found = True
            if found == False:
                dict[i] = 1
        count  = 0
        while count < k:
            max = 0
            i = 0
            val = 0
            for i in dict:
                if dict[i] > max:
                    max = dict[i]
                    val = i
            output.append(val)
            count += 1
            dict.pop(val)
        return output