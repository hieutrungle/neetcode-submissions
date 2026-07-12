class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))


    def rob1(self, nums):
        rob1, rob2 = 0, 0
        
        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2