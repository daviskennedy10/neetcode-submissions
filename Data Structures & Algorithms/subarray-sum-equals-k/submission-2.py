class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        curr_sum = 0
        count = 0
        check = {}

        for i in range(n):
            curr_sum += nums[i]
            prefix[i] = curr_sum
            if prefix[i] == k:
                count +=1
            if (prefix[i] - k) in check:
                count += check[prefix[i]-k]
            check[prefix[i]] = check.get(prefix[i],0) + 1
        print(prefix)

            
        return count


