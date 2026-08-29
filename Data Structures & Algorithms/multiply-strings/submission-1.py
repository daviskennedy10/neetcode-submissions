class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        n = len(num1)
        m = len(num2)

        res = [0] * (m+n)

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                digit = int(num1[i]) * int(num2[j])
                total = digit + res[i+j+1]
                res[i+j] += total // 10
                res[i+j+1] = total % 10
        beg = 0
        while res[beg] == 0:
            beg+=1
        res = map(str, res[beg:])
        return "".join(res)
