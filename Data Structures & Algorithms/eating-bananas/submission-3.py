class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highest = max(piles)
        low, high = 1, highest
        res = h
        while low<=high:
            mid = (low+high)//2
            total = 0
            for num in piles:
                total += math.ceil(num/mid)
            if total <= h:
                high = mid - 1
                res = mid
            else:
                low = mid + 1
        return res
