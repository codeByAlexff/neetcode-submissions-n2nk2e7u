class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Convert this into a set
        #Sets dont allow duplicates

        return len(set(nums)) < len(nums)