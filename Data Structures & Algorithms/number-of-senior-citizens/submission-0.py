class Solution:
    def countSeniors(self, details: List[str]) -> int:
        n = len(details)
        count = 0
        for i in range(n):
            info = details[i]
            age = info[11:13]
            number = int("".join(age))
            if number > 60:
                count +=1
        return count
