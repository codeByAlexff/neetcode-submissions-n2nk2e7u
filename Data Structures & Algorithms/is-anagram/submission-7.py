class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        #If different in length then not anagram

        if sorted(s) == sorted(t) and len(sorted(s)) == len(sorted(t)):
            return True
        else:
            return False
