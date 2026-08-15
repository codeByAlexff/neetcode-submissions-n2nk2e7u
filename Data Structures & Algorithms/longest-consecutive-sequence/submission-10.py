class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Cant sort as sorting is O(n log n)

        #Add number into sequence
        #count sequence digits
        #Biggest sequence is result


        sequence = set(nums)
        longest = 0


        #Iterate through List
        for num in nums:
            #Check if start of sequence
            if num - 1 not in sequence:
                #If it is restart length
                length = 0
                #while 
                while (num + length) in sequence:
                    length += 1
                longest = max(length, longest)
        return longest


                


                

                

