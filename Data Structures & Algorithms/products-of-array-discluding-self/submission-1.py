class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [0] * len(nums)
        zeros = []
        pre = 1
        post = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
                pre = product
                post = 1
                i += 1
            else:
                product = product * nums[i]
                post = post * nums[i]
        if len(zeros) > 1:
            return res
        elif len(zeros) == 1:
            res[zeros[0]] = pre * post
        else:
            for j in range(len(nums)):
                res[j] = product // nums[j]
        return res