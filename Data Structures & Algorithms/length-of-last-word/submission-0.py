class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip()
        n = len(word)
        size = 0
        print("\"" + word + "\"")
        for i in range(n-1,-1,-1):
            print(word[i])
            if word[i] == " ":
                break
            size +=1
        return size