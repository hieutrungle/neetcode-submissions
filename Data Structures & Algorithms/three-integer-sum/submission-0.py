class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = set([])
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return list(res)