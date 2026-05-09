class Solution:
    def reverseBits(self, n: int) -> int:

        res = ""
        for i in range(32):
            bit = n & 1
            res += str(bit)
            n >>=1
        return int(res,2)
        