class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minusstones = [-stone for stone in stones]
        heapq.heapify(minusstones)
        while len(minusstones) > 1:
            first = heapq.heappop(minusstones)
            second = heapq.heappop(minusstones)
            first = first - second
            heapq.heappush(minusstones, first)
        if not minusstones:
            return 0
        return -heapq.heappop(minusstones)
