class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        ans = 0

        while l<r:
            h_l, h_r = heights[l], heights[r]
            trapped_water = min(h_l, h_r) * (r - l)
            ans = max(ans, trapped_water)

            if h_l < h_r:
                l+=1
            else:
                r-=1
        return ans