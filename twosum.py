#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''res=[]
        #inserting the index and value in to the dict
        d=dict()
        for x in range(0,len(nums)):
            d[nums[x]]=x
        print(d)

        for i in range(0,len(nums)):
            if target-nums[i] in d:
                res=[i,d.get(target-nums[i])]
                if res[0]!=res[1]:
                    return res'''
        ###REVISION
        d=dict()
        for i in range(0,len(nums)):
            d[nums[i]]=i
        for i in range(0,len(nums)):
            if target-nums[i] in d and i!=d[target-nums[i]]:
                return [i,d[target-nums[i]]]
        return [-1,-1]
                
