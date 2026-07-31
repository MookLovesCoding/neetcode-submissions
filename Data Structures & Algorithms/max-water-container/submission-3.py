class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            curr = (r - l) * height
            area = max(area, curr)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area