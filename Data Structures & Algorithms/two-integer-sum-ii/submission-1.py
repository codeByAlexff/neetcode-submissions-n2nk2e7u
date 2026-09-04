class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}

        for num in range(len(numbers)):
            diff = target - numbers[num]
            if diff in seen:
                return [seen[diff] + 1, num + 1]
            seen[numbers[num]] = num

        