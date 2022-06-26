# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''pre are nodes in the previous level.
q are node in the current level.

When current level are empty,
the previous level are the deepest leaves.'''
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            pre = q
            current = []
            for p in q:
                for child in [p.left, p.right] :
                    if child:
                        current.append(child)
            q = current
            
        return sum(node.val for node in pre)