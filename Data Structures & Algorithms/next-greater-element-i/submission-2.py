class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        highest_b = max(nums2)
        n = len(nums1)
        m = len(nums2)
        res = []
        j = 0
        fast = {}
        for s in range(m):
            fast[nums2[s]] = s
        for i in range(n):
            if nums1[i] == highest_b:
                res.append(-1)
            else:
                found = False
                start = fast[nums1[i]]+1
                for z in range(start,m):
                    if nums2[z] > nums1[i]:
                        res.append(nums2[z])
                        found = True
                        break
                if not found:
                    res.append(-1)
                

        return res
