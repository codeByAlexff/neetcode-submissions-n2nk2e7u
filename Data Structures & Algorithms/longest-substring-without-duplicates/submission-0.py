class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hs = set()
        L,R = 0,0
        max_length = 0
        while R < len(s):
            if s[R] not in hs:
                hs.add(s[R])
                R += 1
            else:
                hs.remove(s[L])
                L += 1
            max_length = max(max_length, R-L)
        return max_length


