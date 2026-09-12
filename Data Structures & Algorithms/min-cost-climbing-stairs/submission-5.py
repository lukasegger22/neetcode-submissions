class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step = cost[1]
        two_step = cost[0]
        for i in range(2,len(cost)):
            min_cost = min(two_step, one_step)+cost[i]
            two_step, one_step = one_step, min_cost
        return min(one_step, two_step)