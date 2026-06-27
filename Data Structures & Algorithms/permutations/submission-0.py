class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        n = len(nums)

        def dfs(arr, ans):
            if len(ans) == n:
                self.res.append(ans.copy())
                return

            for i, num in enumerate(arr):
                ans.append(num)
                dfs(arr[:i] + arr[i + 1:], ans)
                ans.pop()
            return

        dfs(nums, [])
        return self.res