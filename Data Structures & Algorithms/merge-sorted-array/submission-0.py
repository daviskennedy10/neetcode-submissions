class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0,0
        res = []

        while p2 < n and p1 < m:
            if nums2[p2] <= nums1[p1]:
                res.append(nums2[p2])
                p2+=1
            else:
                res.append(nums1[p1])
                p1+=1
        
        while p1 < m:
            res.append(nums1[p1])
            p1+=1
        while p2 < n:
            res.append(nums2[p2])
            p2+=1
        for r in range(len(res)):
            nums1[r] = res[r]
        
        

