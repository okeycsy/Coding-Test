class Solution:
    def dfs(self, grid, i:int, j:int)->int:
        if i<0 or i>=len(grid) or \
            j<0 or j>=len(grid[0]) or \
            grid[i][j]!='1':
            return
        #위의 것은 종료조건

        grid[i][j]='#'
        for i in range(len(grid)):
            print(grid[i])

        print('\n\n')

        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)

    def numIslands(self,grid)->int:
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count+=1

        return count


S = Solution()
S.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])