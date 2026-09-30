class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int

        [3,6,7,11] h=8  1,2,3,4,5,6,7,8 count = 3 + 6 = 9
        count = 0
        for loop from 1 to max(piles):
            for loop through piles:
                if element < i:
                    count += 1
                else:
                    count += element // i
                and if count exceeds h:
                    break out of the foor loop
            return i
        return max(piles)

        """
        n = len(piles)
        highest = max(piles)
        count = 0
        low = 1
        high = max(piles)
        res = high
        while low <= high:
            count = 0
            mid = (low + high) // 2
            for pile in piles:
                adder = math.ceil(pile/mid)
                count += adder
            if count <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return res
        