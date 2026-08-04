class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        curl = 0
        length = ''
        i = 0
        while i < len(s):
            if s[i] != '#':
                length += s[i]
                i += 1
            else:
                curl = int(length)
                res.append(s[i + 1:i + curl + 1])
                length = ''
                i += curl + 1
        return res