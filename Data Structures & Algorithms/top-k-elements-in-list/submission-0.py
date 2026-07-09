class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        idk = []
        for num in freq:
            idk.append((freq[num], num))
        idk.sort()
        result = []
        for i in range(k):
            result.append(idk.pop()[1])
        return result
