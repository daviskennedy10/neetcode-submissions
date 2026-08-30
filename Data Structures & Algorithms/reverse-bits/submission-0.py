class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            num = n & 1
            n >>= 1
            res <<= 1
            res = res + num
            
        return res