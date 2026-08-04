class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] < nums[l]:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        return res
            