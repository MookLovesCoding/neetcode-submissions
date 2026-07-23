class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            currHeight = min(heights[l], heights[r])
            currArea = (r - l) * currHeight
            if currArea > area:
                area = currArea
            if heights[l] <= heights [r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1

        return area
