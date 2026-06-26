class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res = []
        nums.sort()

        def backtrack(i, total, arr):
            if total == target:
                self.res.append(arr.copy())
                return
            if i >= len(nums) or total > target:
                return

            arr.append(nums[i])
            backtrack(i, total + nums[i], arr)
            arr.pop()
            backtrack(i + 1, total, arr)

        backtrack(0, 0, [])
        return self.res