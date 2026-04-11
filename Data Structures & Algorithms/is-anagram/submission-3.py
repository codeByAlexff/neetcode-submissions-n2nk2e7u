class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #If lengths are not the same return False
        if len(s) != len(t):
            return False
        
        #Initialize two hash maps for s and t
        countS, countT = {}, {}

        #Iterate through every character in the length of s
        for i in range(len(s)):
            #Store every character seen into the hash map
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        #Compare characters for return
        return countS == countT



        