
#https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #bruteforce
        '''maxs=-float('inf')
        for i in range(0,len(nums)):
            prdt=1
            for j in range(i,len(nums)):
                prdt=prdt*nums[j]
                maxs=max(maxs,prdt)
        return maxs'''
        #trying prefix sum method here
        '''if len(nums)==1:
            return nums[0]
        l=len(nums)
        ps=[-1]*l
        ps[0]=nums[0]
        maxs=-float('inf')
        for i in range(1,len(nums)):
            ps[i]=ps[i-1]*nums[i]
            maxs=max(maxs,ps[i])
        return maxs'''
        #using kinda kadanes alg
        '''maxending=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            maxending=max(maxending*nums[i],nums[i])
            res=max(maxending,res)
        
        return res'''
        ###above solutions are trail, nothing completely executed, bruteforce jus did bit TLE

        #striver
        prefix=1
        suffix=1
        maxs=-float('inf')
        for i in range(0,len(nums)):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1

            prefix=prefix*nums[i]
            suffix=suffix*nums[len(nums)-i-1]
            maxs=max(maxs,max(prefix,suffix))
        return maxs
