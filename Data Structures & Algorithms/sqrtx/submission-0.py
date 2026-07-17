class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        while(low <= high):
            mid = (low+high)//2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                high = mid -1
            else:
                low = mid+1
        if low*low > x:
            return low-1
        else:
            return low
