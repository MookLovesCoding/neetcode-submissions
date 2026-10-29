class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        unique_words = {}
        for word in strs:
            word_hash = [0] * 26
            for letter in word:
                number_letter = ord(letter) - ord('a')
                word_hash[number_letter] += 1
            actual_hash = tuple(word_hash)
            if actual_hash not in unique_words:
                unique_words[actual_hash] = [word]
            else:
                unique_words[actual_hash].append(word)
        for word in unique_words:
            output.append(unique_words[word])
        return output