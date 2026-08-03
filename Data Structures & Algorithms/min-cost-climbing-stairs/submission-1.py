class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step = 0
        two_step = 0
        for i in range(2, len(cost)+1):
            current_min = min(cost[i-1]+one_step, cost[i-2]+two_step)
            two_step, one_step = one_step, current_min
        return one_step