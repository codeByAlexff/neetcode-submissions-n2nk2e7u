class Solution:
    def isValid(self, s: str) -> bool:

        #Stack Approach

        #Initialize stack
        stack = []

        #Initialize dictionary matching the closing to opening symbol
        closeToOpen = {")" : "(", "]": "[", "}": "{"}

        #Iterate through every character in s
        for c in s:

            #If the character is inside the dictionary made
            if c in closeToOpen:

                #Check if the stack and the last element equal to the char
                #Previously selected in the dictionary
                if stack and stack[-1] == closeToOpen[c]:
                    #If it matches pop to the stack
                    stack.pop()
                #Else return false as symbols dont match
                else:
                    return False
            #Else if char is NOT in dictionary
            else:
                #Append to the stack
                stack.append(c)
        #For every char return true if not stack
        #Else return false
        return True if not stack else False
        