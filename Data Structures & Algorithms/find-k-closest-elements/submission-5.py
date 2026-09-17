class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        if x <= arr[0]:
            res = []
            for i in range(k):
                res.append(arr[i])
            return res
        check = {}
        closest = float("inf")
        idx = 0
        for r in range(len(arr)):
            if abs(x-arr[r]) < closest:
                closest = abs(x-arr[r])
                idx = r
    
        print(closest)

        count = 0
        res = []
        l,r = idx, idx+1
        while l >= 0 and r < len(arr):
            if abs(x-arr[l]) <= abs(x-arr[r]):
                res.append(arr[l])
                l-=1
                count +=1
            else:
                res.append(arr[r])
                r+=1
                count +=1
                
            if count == k:
                break
        while count < k and l >= 0:
            res.append(arr[l])
            l-=1
            count +=1
        while count < k and r < len(arr):
            res.append(arr[r])
            r+=1
            count +=1

        res.sort()
        return res

