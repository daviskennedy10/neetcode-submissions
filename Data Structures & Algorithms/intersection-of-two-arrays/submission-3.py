class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        if not nums2 or not nums1:
            return []
        checker = set()
        if len(nums1) < len(nums2):
            checker= set(nums2)
            use = nums1
        else:
            checker = set(nums1)
            use = nums2
        
        for i in range(len(use)):
            if use[i] in checker:
                res.add(use[i])
        print(list(res))
        return list(res)