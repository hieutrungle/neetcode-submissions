class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        n = len(nums)
        def backtrack(start, arr):
            self.res.append(arr.copy())
            for i in range(start, n):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
        
        backtrack(0, [])
        return self.res