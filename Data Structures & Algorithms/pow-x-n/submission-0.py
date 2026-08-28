class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def sqrt(x,n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            power = sqrt(x,n//2)
            if n % 2 != 0:
                return x * power * power
            else:
                return power * power
        res = sqrt(x,abs(n))
        if n > 0:
            return res
        else:
            return 1/res