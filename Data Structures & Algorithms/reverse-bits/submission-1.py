class Solution:
    def reverseBits(self, n: int) -> int:
        
        #Initializing result for storing
        res = ""

        #Looping through the integer
        for i in range(32):
            #Sets each bit to 1 if both are 1
            bit = n & 1
            #Add the bit as a string to the result var
            res += str(bit)
            #Signed right shift
            n >>=1
        return int(res,2)
        