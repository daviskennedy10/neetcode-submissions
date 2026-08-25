class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        res = []
        intervals.sort()
        res.append(intervals[0])
        if n <= 1:
            return intervals
        
        print(intervals)
        for i in range(1,n):
            start = intervals[i][0]
            end = intervals[i][1]
            nstart = res[-1][0]
            nend = res[-1][1]

            if start <= nend:
                res[-1] = [min(nstart, start), max(nend,end)]
            
            else:
                res.append(intervals[i])

        return res


        