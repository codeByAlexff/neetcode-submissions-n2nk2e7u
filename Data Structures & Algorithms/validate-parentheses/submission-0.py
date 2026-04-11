class Solution:
    def isValid(self, s: str) -> bool:

        #Brute Force Approach

        #While the string contains the chars required
        while '()' in s or '{}' in s or '[]' in s:
        #remove all occurrences of those pairs
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        #After no more pairs can be removed
        #If string empty return true
        return s == ''
        #Else return false
        