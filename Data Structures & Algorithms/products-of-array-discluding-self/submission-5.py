class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prod = 1
        for i, n in enumerate(nums):
            if i == 0:
                prod *= n
                continue
            res[i] = prod
            prod *= n
        prod = nums[len(nums) - 1]
        for j in range(len(nums) - 2, -1, -1):
            res[j] = prod * res[j]
            prod *= nums[j]
            
        return res
