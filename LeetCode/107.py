"""
107. 二叉树的层次遍历 II

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        queue = [root]
        result = []

        while any(queue):
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)

                if (node.left is not None):
                    queue.append(node.left)
                if (node.right is not None):
                    queue.append(node.right)

            result.append(tmp)

        return result[::-1]


"""
此题解法：这个访问二叉树的方式和102题是一样的，都是广度搜索，只不过结果要求是从树的最底层向上。
偷懒解法：
1、按照102的方式遍历后将结果的list反转即可
2、或者是将tmp的结果每次都插入到result的最前面(这个性能会更好一些)

"""
