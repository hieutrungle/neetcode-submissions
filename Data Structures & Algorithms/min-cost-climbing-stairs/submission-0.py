class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {
            0: cost[0],
            1: cost[1],
        }

        def dfs(n):

            if n in memo:
                return memo[n]

            c = cost[n] if n < len(cost) else 0
            memo[n] = min(dfs(n - 1), dfs(n - 2)) + c
            return memo[n]

        dfs(len(cost))
        return memo[len(cost)]