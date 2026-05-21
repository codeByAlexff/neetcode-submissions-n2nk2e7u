class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #For binary search
        #Initialize left to start of array
        #Initialize right to end of array
        left = 0
        right = len(nums) - 1

        #Loop while left is less than or equal to right
        #As this would mean a number was already found
        while left <= right:
            #Initialize mid as the sum of both indexes and divided by 2
            mid = (left+right) // 2

            #Check if the target is in the middle
            if nums[mid] == target:
                return mid
            
            #If left is less than or equal to mid
            #Then left side is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            #If right is greater than or equal to mid
            #Then right side is sorted
            elif nums[right] >= nums[mid]:
                #If target is smaller than right and bigger than mid
                #Move left forward closer to mid
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                #If not move right forward closer to mid
                else:
                    right = mid - 1
        #Else if target is not in list then return -1
        return -1




        