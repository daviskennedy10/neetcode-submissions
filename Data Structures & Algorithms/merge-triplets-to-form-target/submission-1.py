class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
            n = len(triplets)
            m = len(triplets[0])
        
            res = [0] * m
            highest = max(target)
            r,l = 0,0
            for t in triplets:
                if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                    continue
                res[0] = max(res[0], t[0])
                res[1] = max(res[1], t[1])
                res[2] = max(res[2], t[2])
                
            return res == target
            


        