class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Initialize hash map to store frequency of numbers
        count = {}

        #Loop through every number in the list
        for num in nums:
            #
            count[num] = 1 + count.get(num, 0)

        arr = []
        for i, n in count.items():
            arr.append([n, i])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        