class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or (x,y) in visited or grid[x][y]!="1":
                return
            visited.add((x,y))
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
            return True

        count=0    
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
            
        return count
            