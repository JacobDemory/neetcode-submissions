class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
                return
            
            grid[r][c] = '0'
            
            dfs(r + 1, c) # down
            dfs(r - 1, c) # up
            dfs(r, c + 1) # left
            dfs(r, c - 1) # right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c) # Sink island

        return islands
