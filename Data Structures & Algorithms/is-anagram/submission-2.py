class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, cT = {}, {}
        for char in range(len(s)):
            countS[s[char]] = countS.get(s[char], 0) + 1
            cT[t[char]] = cT.get(t[char], 0) + 1
        return countS == cT