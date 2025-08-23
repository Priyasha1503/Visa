
#https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        vis=set()
        def bfs(r,c):
            que=collections.deque()
            que.append((r,c))
            vis.add((r,c))
            while que:
                delrow,delcol=que.popleft()

                
                directions=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in directions:
                    nrow=delrow+dr #nrow-neighboring rows
                    ncol=delcol+dc
                    if nrow in range(rows) and ncol in range(cols) and grid[nrow][ncol]=='1' and (nrow,ncol) not in vis:
                        que.append((nrow,ncol))
                        vis.add((nrow,ncol))
                    #the below logic works when they ask to include diagonal directions as well
                '''for dr in range(-1,1+1):
                    for dc in range(-1,1+1):
                        nrow=delrow+dr
                        ncol=delcol+dc
                        if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols and grid[nrow][ncol]=="1" and (r,c) not in vis:
                            que.append((nrow,ncol))
                            vis.add((nrow,ncol))'''
                            

        cnt=0
        for r in range(rows):
            for c in range(0,cols):
                if grid[r][c]=='1' and (r,c) not in vis:
                    bfs(r,c)
                    print(r,c)
                    cnt=cnt+1
        print(vis)
        return cnt
