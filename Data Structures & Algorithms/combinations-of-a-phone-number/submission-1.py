class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        container = {}
        container["2"] = "abc"
        container["3"] = "def"
        container["4"] = "ghi"
        container["5"] = "jkl"
        container["6"] = "mno"
        container["7"] = "pqrs"
        container['8'] = "tuv"
        container['9'] = "wxyz"
        subset = []
        res = []

        def dfs(i):
            if len(subset) == len(digits):
                if digits == "":
                    return
                res.append("".join(subset))
                return
            if i >= len(digits):
                return
            
            value = container[digits[i]]
            for j in range(len(value)):
                subset.append(value[j])
                dfs(i+1)
                subset.pop()
        

        dfs(0)
        return res



