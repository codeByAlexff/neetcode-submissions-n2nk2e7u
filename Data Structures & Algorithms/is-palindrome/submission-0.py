class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Initialize new string
        newStr = ""

        #Iterate through every character in the string
        for char in s:
            #Check if character is alphanumerical
            if char.isalnum():
                #IF it is make all characters lowercase in the newStr
                newStr += char.lower()
        #Return if newStr is equals to its reverse
        return newStr == newStr[::-1]