class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            long = 1
            curr = num
            if num - 1 not in numSet:
                while curr + 1 in numSet:
                    long += 1
                    curr += 1
                if long > longest:
                    longest = long
        return longest