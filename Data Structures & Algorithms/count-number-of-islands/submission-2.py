class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #Set up directions for boundaries of movement
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        #Initialize rows, columns
        rows, cols = len(grid), len(grid[0]) #Only one row needs to be counted for list of columns

        #Initialize islands counter
        islands = 0
        
        #Define dfs input rows and columns
        #Set up grid boundary
        #Set cell to "0" to mark as visited
        #Loop to iterate through nearby cells and pass through dfs
        def dfs(r,c):
            if (r<0 or c<0 or r>= rows or c>= cols or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for directionRow, directionCol in directions:
                dfs(r+directionRow, c+directionCol)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands
            