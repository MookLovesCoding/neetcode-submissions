class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr = set(nums)
        return len(nums) != len(curr)