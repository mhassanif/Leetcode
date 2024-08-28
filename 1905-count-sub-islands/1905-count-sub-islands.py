class Solution(object):
    def countSubIslands(self, grid1, grid2):
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid2) or y >= len(grid2[0]) or grid2[x][y] == 0:
                return True
            
            grid2[x][y] = 0  # Mark the cell as visited
            
            # Check if it's a valid sub-island part by ensuring grid1 also has a '1'
            isSubIsland = grid1[x][y] == 1
            
            # Explore all 4 directions (up, down, left, right)
            isSubIsland = dfs(x + 1, y) and isSubIsland
            isSubIsland = dfs(x - 1, y) and isSubIsland
            isSubIsland = dfs(x, y + 1) and isSubIsland
            isSubIsland = dfs(x, y - 1) and isSubIsland
            
            return isSubIsland
        
        subIslandCount = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:  # Start a DFS for each unvisited land cell
                    if dfs(i, j):
                        subIslandCount += 1
        
        return subIslandCount
