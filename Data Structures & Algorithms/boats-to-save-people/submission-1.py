class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        count = 0
        weight = 0
        l,r = 0,n-1
        persons = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                count +=1
                r-=1
                l+=1
            else:
                count +=1
                r -=1
        return count 