class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        curr = set()
        for r in range(len(s)):
            if s[r] not in curr:
                curr.add(s[r])
            else:
                while s[r] in curr:
                    curr.remove(s[l])
                    l += 1
                curr.add(s[r])
            longest = max(longest, len(curr))
        return longest
