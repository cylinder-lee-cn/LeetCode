"""
872. 叶子相似的树

请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

872-1.png
举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

提示：
给定的两颗树可能会有 1 到 100 个结点。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def dfs(node):
            if (node is not None):
                if (node.left is None and node.right is None):
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


"""
此题解法（源自官网）：
首先，让我们找出给定的两个树的叶值序列。之后，我们可以比较它们，看看它们是否相等。

要找出树的叶值序列，我们可以使用深度优先搜索。
如果结点是叶子，那么 dfs 函数会写入结点的值，然后递归地探索每个子结点。
这可以保证按从左到右的顺序访问每片叶子，因为在右子树结点之前完全探索了左子树结点。
"""
