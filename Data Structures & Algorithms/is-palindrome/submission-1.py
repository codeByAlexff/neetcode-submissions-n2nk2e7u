class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Initialize new string
        newStr = ""

        #Loop through every character in the string
        for char in s:
            #Check if the character is alphanumeric
            if char .isalnum():
                #Put char in lowercase inside the new string
                newStr += char.lower()
        #Check if the new string equals its reverse
        return newStr == newStr[::-1]

        