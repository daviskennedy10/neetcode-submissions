class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]
            nstart = newInterval[0]
            nend = newInterval[1]

            if nend < start:
                res.append([nstart,nend])
                return res + intervals[i:]
            elif nstart > end:
                res.append([start,end])
            else:
                newInterval = [min(nstart,start), max(nend,end)]
        res.append(newInterval)
        return res


