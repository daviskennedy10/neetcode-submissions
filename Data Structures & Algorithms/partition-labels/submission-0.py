class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        check = Counter(s)
        count = 0
        res = []
        current_goal = 0
        for i in range(len(s)):
            check[s[i]] = i

        for i in range(len(s)):
            letter = s[i]
            count +=1
            if check[letter] > current_goal:
                current_goal = check[letter]
            if i == current_goal:
                res.append(count)
                count = 0
            
        return res

        
        