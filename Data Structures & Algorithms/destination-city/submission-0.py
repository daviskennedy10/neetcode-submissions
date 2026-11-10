class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        n = len(paths)
        src = set()
        dest = set()
        for start,end in paths:
            src.add(start)
            dest.add(end)
        
        for place in dest:
            if place not in src:
                return place
        
        return dest[-1]
