class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        count = 0
        use = intervals[0]

        for i in range(1,n):
            start = intervals[i][0]
            end = intervals[i][1]

            pstart = use[0]
            pend = use[1]

            if start < pend:
                count +=1
                if end < pend:
                    use = [start,end]
                else:
                    use = [pstart,pend]

            else:
                use = intervals[i]
        return count
