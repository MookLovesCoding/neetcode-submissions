class Solution:

    def encode(self, strs: List[str]) -> str:
        whole = ""
        for word in strs:
            length = len(word)
            whole += str(length) + "#" + word
        return whole

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i <len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = j + length + 1
            decoded.append(s[i:j])
            i = j
        return decoded
