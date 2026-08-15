class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Initialize 2 pointers
        #left is start of List
        #right is end of list
        l, r = 0, len(numbers) - 1

        #while left is less than right
        while l < r:
            #if their addition is less than target move left pointer
            if numbers[l] + numbers[r] < target:
                l += 1
            #if their addition is greater move right pointer
            elif numbers[l] + numbers[r] > target:
                r -= 1
            #if they are the same return their indexes
            #because of 1-indexing we add 1 to their indexes
            else:
                return [l + 1, r + 1]

                


        