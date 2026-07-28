class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = {}
        for i,v in enumerate(nums):
            if v in check:
                if abs(check[v] - i) <= k:
                    return True
            
            check[v] = i
        return False