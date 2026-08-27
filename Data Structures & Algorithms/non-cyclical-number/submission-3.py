class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        def sum_squares(num):
            total = 0
            digits = []
            while num > 0:
                last_digit = num % 10
                digits.append(last_digit*last_digit)
                num = num // 10
            return sum(digits)
        found = False
        use = n
        while not found:
            total = sum_squares(use)
            if total == 1:
                found = True
                return True
            if total in check:
                return False
            check.add(total)
            use = total

        return found

