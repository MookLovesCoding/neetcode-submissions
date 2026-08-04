class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            curr = [0] * 26
            for i in range(len(word)):
                letter = ord(word[i]) - ord('a')
                curr[letter] += 1
            res[tuple(curr)].append(word)
        return list(res.values())