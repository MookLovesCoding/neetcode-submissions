class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        res = []
        for i, num in enumerate(sort):
            if i > 0 and num == sort[i - 1]:
                continue
            l, r = i + 1, len(sort) - 1
            while l < r:
                threesum = num + sort[l] + sort[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([num, sort[l], sort[r]])
                    l += 1
                    while sort[l] == sort[l - 1] and l < r:
                        l += 1
        return res