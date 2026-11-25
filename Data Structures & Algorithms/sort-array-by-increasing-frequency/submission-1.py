class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mapper = Counter(nums)
        sorted_map = sorted(mapper.items(), key=lambda x: (x[1],-x[0]))
        print(sorted_map)
        res = []
        for k,v in sorted_map:
            for i in range(v):
                res.append(k)
        return res