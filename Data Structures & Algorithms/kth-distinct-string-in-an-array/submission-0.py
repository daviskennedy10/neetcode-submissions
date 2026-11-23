class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mapper = Counter(arr)

        count = 0
        print(mapper)
        for key,val in mapper.items():
            if val == 1:
                
                count +=1
                print(count)
                print(key)
                if count == k:
                    return key
        return ""