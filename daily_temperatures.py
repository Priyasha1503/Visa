
#https://leetcode.com/problems/daily-temperatures/submissions/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        stack=[]
        nums=temperatures
        for i in range(len(nums)-1,-1,-1):
            
            while stack!=[] and stack[-1][0]<=nums[i]:
                stack.pop()
            if stack==[]:
                res.append(0)
            else:
                res.append(abs(stack[-1][1]-i))
            stack.append((nums[i],i))
        return res[::-1]
