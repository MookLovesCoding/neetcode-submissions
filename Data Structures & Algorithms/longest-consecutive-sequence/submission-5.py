class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numSet:
                curr = num
                long = 0
                while curr in numSet:
                    long += 1
                    curr += 1
                longest = max(longest, long)
        return longest