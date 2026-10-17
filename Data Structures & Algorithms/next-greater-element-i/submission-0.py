class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        highest_b = max(nums2)
        n = len(nums1)
        m = len(nums2)
        res = []
        j = 0
        for i in range(n):
            print(f"{nums1[i]}, i")
            if nums1[i] == highest_b:
                res.append(-1)
            else:
                for j in range(m):
                    print(f"{nums2[j]}, j")
                    found = False
                    if nums2[j] == nums1[i]:
                        for z in range(j+1,m):
                            print(f"{nums2[z]}, z")
                            if nums2[z] > nums1[i]:
                                res.append(nums2[z])
                                found = True
                                break
                        if not found:
                            res.append(-1)
                        break

        return res
