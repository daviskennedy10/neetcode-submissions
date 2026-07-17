class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        brute = []
        for i in range(len(nums1)):
            brute.append(nums1[i])
        for j in range(len(nums2)):
            brute.append(nums2[j])
        brute.sort()
        low, high = 0, len(brute)-1
        mid = (low+high)//2
        if len(brute) % 2 ==0:
            return (brute[mid] + brute[mid+1])/2
        else:
            return brute[mid]
