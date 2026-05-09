class Solution:
    def countBits(self, n: int) -> List[int]:

        output = []
        for num in range(n+1):
            output.append(bin(num).count('1'))
        return output
        