"""
404. 左叶子之和

计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sumleft = 0

    def preorderTraversal(self, root, p):
        if (root is not None):
            if (p == 'l' and root.left is None and root.right is None):
                self.sumleft = self.sumleft + root.val
            self.preorderTraversal(root.left, 'l')
            self.preorderTraversal(root.right, 'r')

        return self.sumleft

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None):
            return 0

        self.preorderTraversal(root, 'c')
        return self.sumleft


"""
此题解法：
* 选取一个任意的遍历方式，这里选了前序遍历
* 递归函数里增加一个参数表示分支的位置（c：根，l：左，r：右）
* 当是左分支时，检查一下这个节点是否还有子树，如果没有就是一个左叶子。
  累加这个节点的值。
  
"""
