"""
110. 平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def deep(tnode):
            if tnode is None:
                return 0

            left = deep(tnode.left)
            right = deep(tnode.right)

            if (left == -1 or right == -1 or abs(left - right) > 1):
                return -1

            return max(left, right) + 1

        return deep(root) != -1


"""
此题解法：
* 使用递归方式
* 递归求节点的深度，没递归一次，就比较一下左右子树的深度，如果差值超过1，那就返回-1
* 否则就将总深度+1，然后继续递归
* 最后看看计算的深度是否是-1
"""
