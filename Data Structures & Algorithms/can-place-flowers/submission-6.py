class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        k = len(flowerbed)
        for i in range(k-1):
            if flowerbed[i] == 1:
                continue
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n-=1
            elif flowerbed[i] == 0:
                if i > 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n-=1
        if flowerbed[-1] == 0 and flowerbed[k-2] == 0:
            n-=1
        print(flowerbed)
        print(n)
        return n <= 0