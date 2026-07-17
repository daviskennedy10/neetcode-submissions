class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        highest = sum(weights)
        low, high = max(weights), highest
        res = high
        while low <= high:
            mid = (low+high)//2
            count = 1
            add = 0
            for w in weights:
                add+=w
                if add > mid:
                    add = w
                    count+=1

            if count <= days:
                res = mid
                high = mid - 1
                
            else:
                low = mid + 1
        return res
            
            