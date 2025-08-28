
#https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=dict()
        stack=[nums2[-1]]
        result=[]
        #first finding all the next greater elmenets of nums2
        for i in range(len(nums2)-1,-1,-1):

            while stack!=[] and stack[-1]<=nums2[i]:
                stack.pop()
            if stack==[]:
                d[nums2[i]]=-1
            else:
                d[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        print(d)
        for i in range(0,len(nums1)):
            x=d[nums1[i]]
            result.append(x)
        return result
