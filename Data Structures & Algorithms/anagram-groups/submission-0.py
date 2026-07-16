class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        output = []
        for i in strs:
            tmp = "".join(sorted(i))
            found = False
            for j in dict:
                if tmp == j:
                    dict[j].append(i)
                    found = True
            if found == False:    
                dict[tmp] = [i]
        for i in dict:
            output.append(dict[i])
        return output
            
        