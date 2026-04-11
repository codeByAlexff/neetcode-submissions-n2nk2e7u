class Solution:
    def isValid(self, s: str) -> bool:

        #Initialize dictionary with open and close symbols
        p_map = {"]": "[", ")": "(", "}": "{"}

        #Initialize stack for symbols to add
        stack = []

        #For every char in s
        for c in s:

            #Check if the char is inside the dictionary of symbols
            if c in p_map:

                #Check if stack is empty or 
                #A removed element of the top of the stack
                #Is NOT equal to the char inside the dictionary
                if not stack or stack.pop() != p_map[c]:

                    #If above is true return False
                    return False
            #If c NOT in dictionary
            else:
                #Append to the stack
                stack.append(c)
        #After every symbol return true if stack is empty
        #If it's not empty return false
        return True if not stack else False
        