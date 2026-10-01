class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        low = max(nums)
        high = sum(nums)
        
        def count_subarrays(max_sum_allowed):
            count = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > max_sum_allowed:
                    count +=1
                    curr_sum = num
                else:
                    
                    curr_sum += num
            return count


        while low <= high:
            mid = (low+ high) // 2
            if count_subarrays(mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid +1
        return ans