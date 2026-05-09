class Solution:
    def countBits(self, n: int) -> List[int]:

        output = []
        for num in range(n+1):
            binary = bin(num)
            one = binary.count('1')
            output.append(one)
        return output

        