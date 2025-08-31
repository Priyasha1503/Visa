
#https://leetcode.com/problems/backspace-string-compare/description/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def func(strs,stack):
            for i in strs:
                if i =='#':
                    if stack!=[]:
                        stack.pop()
                else:
                    stack.append(i)
            return "".join(stack)

        stack_s=[]
        stack_t=[]

        x=func(s,stack_s)
        y=func(t,stack_t)
        print(x,y)
        if x==y:
            return True
        else:
            return False


