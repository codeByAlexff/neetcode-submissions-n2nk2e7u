class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Sort strings
        return sorted(s) == sorted(t)
        #Compare letters
        #If they match then return True
        #Else False


        

        