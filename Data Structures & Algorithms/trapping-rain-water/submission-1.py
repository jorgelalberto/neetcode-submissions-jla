class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_l = height[l]
        max_r = height[r]
        trapped_water = 0

        while l<r:
            if height[l] < height[r]:
                trapped_water += max(max_l - height[l+1], 0)
                max_l = max(max_l, height[l+1])
                l+=1
            else:
                trapped_water += max(max_r - height[r-1], 0)
                max_r = max(max_r, height[r-1])
                r-=1
        
        return trapped_water