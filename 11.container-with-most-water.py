from typing import List

#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

