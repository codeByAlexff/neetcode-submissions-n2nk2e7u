class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #Create a hash set to remove duplicates

        #set(nums)

        #Compare the length of this set to the length of the list

        #len(set(nums)) is smaller than len(nums)
        #This means the duplicate was deleted so there WAS a duplicate
        return len(set(nums)) < len(nums)
        