class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        length = 0
        l = 0
        most = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            most = max(most, window[s[r]])
            while (r - l + 1) - most > k:
                window[s[l]] = window.get(s[l], 0) - 1
                l += 1
                most = max(most, window[s[l]])
            length = max(length, (r - l + 1))
        return length