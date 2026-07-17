class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        brute = nums1 + nums2
        brute.sort()
        low, high = 0, len(brute)-1
        mid = (low+high)//2
        if len(brute) % 2 ==0:
            return (brute[mid] + brute[mid+1])/2
        else:
            return brute[mid]
