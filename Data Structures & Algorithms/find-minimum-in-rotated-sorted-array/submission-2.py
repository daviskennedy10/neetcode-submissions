class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[low]> nums[high]:
                if nums[mid]> nums[high]:
                    low = mid+1
                else:
                    high = mid

            else:
                return nums[low]
        return nums[low]