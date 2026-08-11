class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Create dict with list as key
        res = defaultdict(list)

        for i in strs:
            sortedS = "".join(sorted(i))
            res[sortedS].append(i)
        return list(res.values())






