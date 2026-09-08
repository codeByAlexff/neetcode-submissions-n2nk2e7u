class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for c in t:
            freq[c] = freq.get(c , 0) - 1
            if not any(freq.values()):
                return True
        return False

