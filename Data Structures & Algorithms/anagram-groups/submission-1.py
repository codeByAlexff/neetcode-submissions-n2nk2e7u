class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for c in strs:
            sortedC = tuple(sorted(c))
            if sortedC in dic:

                dic[sortedC].append(c)

            else:
                dic[sortedC] = [c]
        return list(dic.values())
        
        