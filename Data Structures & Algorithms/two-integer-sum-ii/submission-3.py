class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Two pointers
        l , r = 0, (len(numbers) - 1)

        #If nums[0] + nums[n - 1] > target
        #then nums[n - 1] cannot be in array
        #Because nums[n - 1] is largest element in array
        #Base case:
        #while nums[0] + nums[n - 1] < target
        while l < r:
            currSum = numbers[l] + numbers[r]
            if (currSum > target):
                r -= 1
            elif (currSum < target):
                l += 1
            elif (currSum == target):
                return [l + 1, r + 1]


        