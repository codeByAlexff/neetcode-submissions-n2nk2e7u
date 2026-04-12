class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Initializa hash map for each string
        s_dict = {}
        t_dict = {}

        #Check initially if they arent the same length
        #As anagrams need same length
        if len(s) != len(t):
            return False
        #Else start loop
        else:
            #Loop through every char in the length of s
            for i in range(len(s)):
                #For every char
                #Get the char in position i
                #Retrieve the count of the char
                #If char exists in the map return count
                #If it doesnt exist return 0
                #Add 1 to the count
                s_dict[s[i]] = s_dict.get(s[i],0) + 1
                t_dict[t[i]] = t_dict.get(t[i],0) + 1
            #If both counts are the same then True
            #Else false
            return s_dict == t_dict


        
        