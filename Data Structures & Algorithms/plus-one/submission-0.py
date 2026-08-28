class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = []

        carry = 1
        for i in range(n-1,-1,-1):
            num = digits[i]
            res.append((num+carry) % 10)
            carry = (num+carry) // 10

        if res[-1] == 0:
            res.append(1)
        res.reverse()
        return res
            