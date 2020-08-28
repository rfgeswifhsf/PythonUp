'''
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        maxDepth = lambda root: 0 if not root else 1+max(maxDepth(root.left), maxDepth(root.right))
        tmp = maxDepth(root.left) - maxDepth(root.right)
        return tmp in (-1, 0, 1) and self.isBalanced(root.left) and self.isBalanced(root.right)

