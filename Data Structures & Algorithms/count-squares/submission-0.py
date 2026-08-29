class CountSquares:

    def __init__(self):
        self.container = {}
        

    def add(self, point: List[int]) -> None:
        pt = (point[0], point[1])
        self.container[pt]= self.container.get(pt,0) + 1
        

    def count(self, point: List[int]) -> int:
        qx, qy = point[0], point[1]
        count = 0
        for (x,y), freq in self.container.items():
            if abs(x-qx) == abs(y-qy) and abs(x-qx) > 0:
                if (x,qy) in self.container and (qx,y) in self.container:
                    count += freq * self.container[(x,qy)] * self.container[(qx,y)] 
                        
        return count



        
