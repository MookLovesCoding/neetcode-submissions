class Solution:
    def findMin(self, nums: List[int]) -> int:
        search = nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = ((r - l) // 2) + l 
            if nums[mid] < search:
                search = nums[mid]
                r = mid
            else:
                l = mid + 1
        return min(search, nums[r])