class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Put the values of nums inside the hashSet
        hashSet = set(nums)

        #Initialize the longest value, 0 by default
        longest = 0

        #Loop through the list
        for num in nums:
            #Initialize current to be the current num iteration
            curr = num
            #Initialize count to after the first num of the sequence
            count = 1
            
            #Check if the number before is in the set, if it is skip the iteration
            if num - 1 in hashSet:
                continue
            #If it's not
            else:
                #Loop while num + 1 is inside the hashSet
                while curr + 1 in hashSet:
                    #Increase current by one
                    curr += 1
                    #Increase count by one
                    count += 1
                #Initialize longest variable to be the max of longest and the count
                longest = max(longest, count)
        #Return the longest variable
        return longest






