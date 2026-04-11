class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #If length of string s does not equal t return False
        if len(s) != len(t):
            return False

        #If both strings sorted are equal return True
        return sorted(s) == sorted(t)



        