"""
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def isMirror(self, rl, rr):
        if (rl is None and rr is None):
            return True
        if (rl is None or rr is None):
            return False
        if (rl.val != rr.val):
            return False
        return (self.isMirror(rl.left, rr.right)
                and self.isMirror(rl.right, rr.left))

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root is None):
            return True

        return self.isMirror(root.left, root.right)


"""
此题解法：此题和100题非常类似，对称的话就是左右对称节点进行比较，也就是左枝和右枝进行比较,右枝和左枝进行比较
。
"""
