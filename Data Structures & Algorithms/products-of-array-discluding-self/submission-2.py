class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1] * size
        prod = 1
        for i in range(size):
            res[i] = prod
            prod = prod * nums[i]
        prod = 1
        for j in range(size - 1, -1, -1):
            res[j] = res[j] * prod
            prod = prod * nums[j]
        return res