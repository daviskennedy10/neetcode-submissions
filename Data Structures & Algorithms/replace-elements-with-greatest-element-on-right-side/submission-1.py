class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        highest = arr[-1]
        for i in range(n-2,-1,-1):
            if arr[i] > highest:
                temp = highest
                highest = arr[i]
                arr[i] = temp
            else:
                arr[i] = highest
            
            
        arr[-1] = -1
        return arr
