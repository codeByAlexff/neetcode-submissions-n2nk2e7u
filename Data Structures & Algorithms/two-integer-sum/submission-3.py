class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for i, n in enumerate(nums):
            miss = target - n
            if miss in hm:
                return [hm[miss], i]
            hm[n] = i
