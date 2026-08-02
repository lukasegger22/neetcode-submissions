class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_steps_back = 0 
        one_step_back = 0
        for i in range(2, len(cost)+1):
            current_cost = min(one_step_back + cost[i-1], two_steps_back + cost[i-2])
            two_steps_back, one_step_back = one_step_back,current_cost
        return one_step_back

