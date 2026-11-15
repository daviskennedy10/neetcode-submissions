class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapper ={}
        n = len(pattern)
        m = len(s)
        s_arr = s.split(" ")
        print(s_arr)
        if n != len(s_arr):
            return False

        for i in range(n):
            if pattern[i] not in mapper:
                if s_arr[i] in mapper.values():
                    return False
                mapper[pattern[i]] = s_arr[i]
            else:
                if s_arr[i] != mapper[pattern[i]]:
                    return False
        print(mapper)
        return True
    
