
#https://leetcode.com/problems/rotate-string/?utm_source=chatgpt.com

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=list(s)
        for i in range(0,len(s)):
            x=s.pop(0)
            s.append(x)
            if s==list(goal):
                return True
        return False


'''abcde
bcdea
cdeab'''

