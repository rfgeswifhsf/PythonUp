# coding:utf-8
class TreeNode(object):
    def __init__(self,left=None,right=None,data=0):
        self.left = left
        self.right = right
        self.data =data



class BTree(object):
    def __init__(self,root=None):
        self.root = root


if __name__ == "__main__":
    node1 = TreeNode(data=1)
    node2 = TreeNode(node1, None, 2)
    node3 = TreeNode(data=3)
    node4 = TreeNode(data=4)
    node5 = TreeNode(node3, node4, 5)
    node6 = TreeNode(node2, node5, 6)
    node7 = TreeNode(node6, None, 7)
    node8 = TreeNode(data=8)
    root = TreeNode(node7, node8, 'root')
    bt = BTree(root)

    print()
