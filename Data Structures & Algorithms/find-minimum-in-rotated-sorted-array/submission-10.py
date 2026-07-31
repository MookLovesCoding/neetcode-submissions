class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = nums[0]
        m = len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if nums[l] < nums[r]:
                smallest = min(nums[l], smallest)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
                if nums[m] < smallest:
                    smallest = nums[m]
        return min(smallest, nums[m])