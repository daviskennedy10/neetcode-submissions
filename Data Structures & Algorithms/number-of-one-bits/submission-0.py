class Solution:
    def hammingWeight(self, n: int) -> int:
        word = str(bin(n))
        count = 0
        for i in range(2,len(word)):
            if word[i] == "1":
                count +=1
        return count