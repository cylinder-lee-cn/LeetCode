"""
111. 二叉树的最小深度

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if (root is None):
            return 0

        if (root.left is None):
            return self.minDepth(root.right) + 1

        if (root.right is None):
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


"""
此题解法：
* 采用递归来遍历二叉树，找到left和right都是None的叶子节点，同时计算深度

* 也可以采用迭代的方法：
        if root is None:
            return 0

        depth = 1
        stack = [root]
        while stack:
            level = []
            for i in stack:
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
                elif not i.left:
                    return depth
            depth += 1
            stack = level[:]
----------------------------------
        if not root:
            return 0

        nodes = [root]
        level = 1
        
        while nodes:
            inner = []
            for node in nodes:
                if not node.left and not node.right:
                    return level
                if node.left:
                    inner.append(node.left)
                if node.right:
                    inner.append(node.right)
            nodes = inner
            level += 1            
"""
