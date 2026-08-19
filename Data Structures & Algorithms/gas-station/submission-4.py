class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        current_tank = 0
        idx = 0
        if sum(cost) > sum(gas):
            return -1

        for i in range(n):
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                idx = i + 1;
                current_tank = 0
        if idx >= n:
            return -1
        else:
            return idx
