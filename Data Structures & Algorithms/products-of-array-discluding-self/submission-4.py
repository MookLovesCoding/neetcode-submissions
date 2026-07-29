class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        prod = nums[0]
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = prod
            prod *= nums[i]
        prod = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            suf[j] = prod
            prod *= nums[j]
        for k in range(len(nums)):
            res[k] = pre[k] * suf[k]
        return res