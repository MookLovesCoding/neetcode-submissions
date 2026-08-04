import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = {}
        counter = 0
        revCounts = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num in counts:
            revCounts[counts[num]].append(num)
        for i in range(len(nums), -1, -1):
            for num in revCounts[i]:
                counter += 1
                res.append(num)
                if counter == k:
                    return res
        return res
