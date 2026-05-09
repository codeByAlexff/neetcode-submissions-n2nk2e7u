class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        expectedSum = n * (n + 1) // 2
        ans = expectedSum - sum(nums)
        return ans

        