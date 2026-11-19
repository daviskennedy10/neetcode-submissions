class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = ["b","a","l","l","o","o","n"]
        freq ={}
        if len(text) < len("balloon"):
            return 0

        for i in range(len(text)):
            if text[i] in balloon:
                if text[i] == "l" or text[i] == "o":
                    freq[text[i]] = freq.get(text[i],0)+ 0.5
                else:
                    freq[text[i]] = freq.get(text[i],0)+1
        
        values = list(freq.values())
        for i in balloon:
            if i not in freq:
                return 0
        print(freq)
        smallest = min(values)
        if smallest <= 0.5:
            return 0
        else:
            return int(smallest)
        
        
