class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if t == "":
            return res
        shortest = len(s) * 2
        correct = 0
        charToCount = {}
        curr = {}
        l = 0
        for char in t:
            charToCount[char] = charToCount.get(char, 0) + 1
        for r in range(len(s)):
            curr[s[r]] = curr.get(s[r], 0) + 1
            if s[r] in charToCount:
                if curr[s[r]] == charToCount[s[r]]:
                    correct += 1
                while correct == len(charToCount):
                    if s[l] in charToCount and curr[s[l]] == charToCount[s[l]]:
                        break
                    curr[s[l]] = curr[s[l]] - 1
                    l += 1
                if r - l + 1 < shortest and correct == len(charToCount):
                    res = s[l:r + 1]
                    shortest = r - l + 1
        return res