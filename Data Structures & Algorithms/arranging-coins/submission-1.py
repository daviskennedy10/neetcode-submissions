class Solution:
    def arrangeCoins(self, n: int) -> int:
        step = 1
        count = 0
        while n > 0:
            if n >= step:
                n -= step
                count +=1
            else:
                return count
            step +=1
        return count