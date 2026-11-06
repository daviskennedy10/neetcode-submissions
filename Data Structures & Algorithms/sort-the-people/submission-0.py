class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        putter = {}

        for i in range(n):
            putter[heights[i]] = names[i]
        
        sorted_map = dict(sorted(putter.items(), key=lambda item: item[0], reverse=True))
        res = list(sorted_map.values())
        return res


       