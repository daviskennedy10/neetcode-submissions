class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        difference = 0
        arr = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in map:
                arr.append(map.get(difference))
                arr.append(i)
                
            map[nums[i]] = i

        return arr