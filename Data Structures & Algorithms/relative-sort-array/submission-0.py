class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        self.mapper = {}
        for i in range(len(arr2)):
            self.mapper[arr2[i]] = i
        for j in range(len(arr1)):
            if arr1[j] not in self.mapper:
                self.mapper[arr1[j]] = float("inf")

        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            half = len(arr) // 2

            first = mergesort(arr[:half])
            second = mergesort(arr[half:])
            return merge(first,second)
                

        def merge(sorted_first, sorted_second):
            i, j = 0,0
            res = []
            while i < len(sorted_first) and j < len(sorted_second):
                if self.mapper[sorted_first[i]] == self.mapper[sorted_second[j]]:
                    if sorted_first[i] <= sorted_second[j]:
                        res.append(sorted_first[i])
                        i+=1
                    else:
                        res.append(sorted_second[j])
                        j+=1

                elif self.mapper[sorted_first[i]] < self.mapper[sorted_second[j]]:
                    res.append(sorted_first[i])
                    i+=1
                else:
                    res.append(sorted_second[j])
                    j+=1
            
            if i < len(sorted_first):
                res.extend(sorted_first[i:])
            if j < len(sorted_second):
                res.extend(sorted_second[j:])

            return res
        
        return mergesort(arr1)
        
        
        


