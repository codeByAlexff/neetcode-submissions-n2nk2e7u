class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashSet = set(nums)
        longest = 0

        for num in nums:
            curr = num
            count = 1
            
            if num - 1 in hashSet:
                continue
            else:
                while curr + 1 in hashSet:
                    curr += 1
                    count += 1
                longest = max(longest, count)
        return longest






