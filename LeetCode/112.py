"""
112. 路径总和

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if (root is None):
            return False

        # if not (root.left or root.right):
        if (root.left is None and root.right is None):
            return (sum == root.val)

        return (self.hasPathSum(root.left, sum - root.val)
                or self.hasPathSum(root.right, sum - root.val))


root = TreeNode(5)
l1 = TreeNode(4)
r1 = TreeNode(8)
l1l = TreeNode(11)
l1ll = TreeNode(7)
l1lr = TreeNode(2)
r1l = TreeNode(13)
r1r = TreeNode(4)
r1rr = TreeNode(1)

root.left = l1
root.right = r1
l1.left = l1l
r1.left = r1l
r1.right = r1r
l1l.left = l1ll
l1l.right = l1lr
r1l.right = r1rr

s = Solution()
print(s.hasPathSum(root, 20))
"""
此题解法：叶子节点的定义就是‘没有子节点’，TreeNode.left is None And TreeNode.right is None
使用递归的算法。
"""
