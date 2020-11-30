class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp = [None,None]
        for x in range(k):
            for i in range(len(grid)):
                if (i-1) == temp[0]:
                    grid[i].insert(0,temp[1])
                if i != len(grid)-1:
                    #continue
                    temp = [i,grid[i].pop()]
                if i == 0:
                    grid[i].insert(0,grid[len(grid)-1].pop())

        return grid 
