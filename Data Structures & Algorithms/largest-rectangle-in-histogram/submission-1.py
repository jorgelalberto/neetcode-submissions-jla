class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        height_to_inds = [None]*(max(heights)+1)
        max_area = 0

        for i, height in enumerate(heights):
            for j in range(1, height+1):
                if height_to_inds[j] and height_to_inds[j]['stop'] == i-1:
                    height_to_inds[j]['stop'] += 1
                    start = height_to_inds[j]['start']
                    stop = height_to_inds[j]['stop']
                    max_area = max(max_area, ((stop+1)-start)*j)
                else:
                    temp_inds = height_to_inds[j]
                    if temp_inds:
                        start = temp_inds['start']
                        stop = temp_inds['stop']
                        max_area = max(max_area, ((stop+1)-start)*j)
                    height_to_inds[j] = {'start': i, 'stop': i}
                    start = height_to_inds[j]['start']
                    stop = height_to_inds[j]['stop']
                    max_area = max(max_area, ((stop+1)-start)*j)
        return max_area