class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        res = []
        curr = 0
        for i, num in enumerate(sort):
            if i > 0 and num == sort[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if sort[l] + sort[r] > -(num):
                    r -= 1
                elif sort[l] + sort[r] < -(num):
                    l += 1
                else:
                    res.append([num, sort[l], sort[r]])
                    l += 1
                    r -= 1
                    while sort[l] == sort[l - 1] and l < r:
                        l += 1
        return res