class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        prod = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            left[i] = prod
            prod *= nums[i]
        prod = 1
        for j in range(len(nums) - 1, -1, -1):
            right[j] = prod
            prod *= nums[j]
        for h in range(len(nums)):
            res[h] = left[h] * right[h]
        return res