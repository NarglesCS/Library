class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        areaGrid = grid
        area = 0
        for i,row in enumerate(grid):
            for j,tower in enumerate(row):
                # eq for area of a single tower
                #(x*4) + 2
                # eq for area of a tower with surrounding towers. As long as they are not taller that main tower.
                #(x*4) + 2 - sum(hTowers)
                otherTowers = 0
                if (i != 0):
                    #top boundary
                    if tower<= grid[i-1][j]:
                        otherTowers += tower
                    else:
                        otherTowers += grid[i-1][j]
                if (i != len(grid[0])-1):
                    #bottom boundary
                    if tower<= grid[i+1][j]:
                        otherTowers += tower
                    else:
                        otherTowers += grid[i+1][j]
                if (j != 0):
                    #left boundary
                    if tower<= grid[i][j-1]:
                        otherTowers += tower
                    else:
                        otherTowers += grid[i][j-1]
                if (j != len(grid)-1):
                    #right boundary
                    if tower<= grid[i][j+1]:
                        otherTowers += tower
                    else:
                        otherTowers += grid[i][j+1]

                if tower != 0:
                    area += (tower*4) + 2 - otherTowers
        return area
