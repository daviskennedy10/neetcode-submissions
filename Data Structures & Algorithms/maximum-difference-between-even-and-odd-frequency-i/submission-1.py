class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        even = []
        odd = []

        for k,v in freq.items():
            if v % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        
        highest_even, highest_odd = max(even), max(odd)
        lowest_even, lowest_odd = min(even), min(odd)

        return highest_odd - lowest_even

        