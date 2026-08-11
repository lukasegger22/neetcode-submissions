class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step_cost = 0
        two_step_cost = 0
        for i in range(2, len(cost)+1):
            min_cost = min(cost[i-1]+one_step_cost, cost[i-2]+two_step_cost)
            two_step_cost, one_step_cost = one_step_cost, min_cost
        return one_step_cost
