
#https://leetcode.com/problems/flood-fill/

'''class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:return []
        res_image=[row[:] for row in image]

        rows,cols=len(image),len(image[0])
        vis=set()
        def bfs(r,c):
            que=collections.deque()
            #changing into the color
            res_image[r][c]=color
            que.append((r,c))
            vis.add((r,c))
            while que:
                delrow,delcol=que.popleft()
                directions=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in directions:
                    nrow,ncol=dr+delrow,dc+delcol
                    if nrow>=0 and ncol>=0 and nrow<rows and ncol<cols and image[nrow][ncol]==image[sr][sc] and (nrow,ncol) not in vis:
                        res_image[nrow][ncol]=color #changing into the color
                        que.append((nrow,ncol))
                        vis.add((nrow,ncol))
        #for r in range(rows):
            #for c in range(cols):
                #if image[r][c]==image[sr][sc] and (r,c) not in vis:
                    #bfs(r,c)
                    ###NO NEED OF ALL THIS, WE COULD DIRECTLY CALL FUNC WITH SR,SC
            #and it again makes the other cells  which isnt related to image[sr][sc] also into color..and changes it
            #example 1: the last row,last col here doesnt need to get changed into 2,becuase it is not connected to image[sr][sc]..but here it still gets converted if we do it like this,ecuase we will again check in main func with the loop if it image[r][c]=image[sr][sc]
                    
        bfs(sr,sc)
        return res_image
        '''
###DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        vis=set()
        res_image=[row[:] for row in image]
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            elif (r,c) in vis:
                return
            elif image[r][c]==image[sr][sc]:
                res_image[r][c]=color
                vis.add((r,c))
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r,c-1)
                return res_image
        dfs(sr,sc)
        return res_image

