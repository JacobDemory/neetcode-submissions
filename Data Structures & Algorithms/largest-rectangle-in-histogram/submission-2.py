class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                height = heights[stack[-1]]
                stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(height * width, max_area)
            stack.append(i)

        return max_area
