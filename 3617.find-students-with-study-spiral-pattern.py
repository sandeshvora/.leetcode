from typing import List
class Solution:
    def findStudentsWithSpiralPattern(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        spiral = []
        visited = [[False]*n for _ in range(m)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        x = y = d = 0
        for _ in range(m*n):
            spiral.append(matrix[x][y])
            visited[x][y] = True
            nx, ny = x + dirs[d][0], y + dirs[d][1]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                x, y = nx, ny
            else:
                d = (d + 1) % 4
                x, y = x + dirs[d][0], y + dirs[d][1]
        # Assuming each row is a student, and spiral pattern means their row matches the spiral order
        result = []
        for i, row in enumerate(matrix):
            if row == spiral[:n]:
                result.append(i)
        return result
    
# @lc code=end
# @lc app id=3617 lang=python3
#
