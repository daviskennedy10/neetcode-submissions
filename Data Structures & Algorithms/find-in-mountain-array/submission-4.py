# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        peak = 0
        low, high = 0, mountainArr.length()-1
        while low < high:
            mid = (low + high) // 2
            if mountainArr.get(mid) > mountainArr.get(mid+1):
                peak = mid
                high = mid
            else:
                low = mid + 1
        
        low, high = 0, peak
        while low <= high:
            mid = (low + high) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                high = mid - 1
            else:
                low = mid + 1
        
        low, high = peak, mountainArr.length()-1
        while low <= high:
            mid = (low + high) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                low = mid + 1
                
            else:
                high = mid - 1
        return -1
