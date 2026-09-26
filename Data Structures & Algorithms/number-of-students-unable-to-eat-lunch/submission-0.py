class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [students.count(0), students.count(1)]

        for s in sandwiches:
            if count[s] > 0:
                count[s] -=1
            else:
                break
        return count[0] + count[1]