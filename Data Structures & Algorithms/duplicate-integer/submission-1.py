class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #a set() is used to create an unordered collection of unique elements
        #a set automatically removes duplicate values
        # it takes list, tuple, string, range or dictionary.
        return len(set(nums)) < len(nums)
        