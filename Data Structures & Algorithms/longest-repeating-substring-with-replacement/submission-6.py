class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        longest = 0
        long = 1
        l = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            long = max(long, seen[s[r]])
            while (r - l) + 1 - long > k:
                seen[s[l]] = seen[s[l]] - 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest