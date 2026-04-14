class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Initialize an empty dictionary res
        res = defaultdict(list)

        #Loop through the list
        for s in strs:
            #Initialize count array with 26 zeros for alphabet
            count = [0] * 26
            #Loop through the character in the word
            for char in s:
                #Every letter of the alphabet is initially 0
                #Every letter found in word
                #Set that 0 to 1 by adding 1 as they are all 0
                count[ord(char) - ord('a')] += 1
            #Ad word to hash map with count as a tuple
            #Count will act as a key to the dictionary res
            res[tuple(count)].append(s)
        #Return values of the hash map as grouped anagrams
        return list(res.values())
        