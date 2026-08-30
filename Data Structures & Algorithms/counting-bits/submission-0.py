class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        output = []
        for i in range(n+1):
            output.append(count(i))
        return output
