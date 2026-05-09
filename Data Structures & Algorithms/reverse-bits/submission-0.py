class Solution:
    def reverseBits(self, n: int) -> int:

        bit = bin(n)[2:].zfill(32)[::-1]
        return int(bit,2)
        