class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        count = 0
        weight = 0
        l,r = 0,n-1
        persons = 0
        while l < r or persons < n:
            if people[l] + people[r] <= limit:
                persons += 2
                count +=1
                r-=1
                l+=1
            else:
                count +=1
                persons +=1
                r -=1
            print(count)
            print(l)
            print(r)
        return count 