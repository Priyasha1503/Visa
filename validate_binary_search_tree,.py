
#https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        low,high=-float('inf'),float('inf')

        def func(root,low,high):
            if root is None:
                return True
            if not low<root.val<high:
                return False
            
            return func(root.left,low,root.val) and func(root.right,root.val,high)
        
        return func(root,low,high)
