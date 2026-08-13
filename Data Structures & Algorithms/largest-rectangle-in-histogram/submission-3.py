class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # {'height': _, 'ind': _}
        max_area = 0

        for i, height in enumerate(heights):
            min_ind = i
            while stack and stack[-1]['height'] > height:
                min_ind = stack[-1]['ind']
                ele = stack.pop()
                area = ele['height'] * (i - ele['ind'])
                max_area = max(max_area, area)
            stack.append({'height': height, 'ind': min_ind})

        for ele in stack:
            height = ele['height']
            ind = ele['ind']
            area = height * (len(heights)-ind)
            max_area = max(max_area, area)

        return max_area