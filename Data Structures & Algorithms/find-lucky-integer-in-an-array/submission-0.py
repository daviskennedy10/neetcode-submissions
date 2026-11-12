class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        sorted_freq = dict(sorted(freq.items(), key = lambda x: x[1], reverse=True))
        holder = []
        highest = float("-inf")
        for k,v in freq.items():
            if k == v:
                highest = max(k,highest)
                holder.append(k)
        return highest if highest > float("-inf") else -1
