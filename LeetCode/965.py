"""
965. 单值二叉树

如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。


示例 1：
输入：[1,1,1,1,1,null,1]

输出：true

示例 2：
输入：[2,2,2,5,2]
输出：false

提示：
给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.nodevalue = []

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.accesstree(root)
        # print(self.nodevalue)
        v = self.nodevalue[0]
        return all(x == v for x in self.nodevalue)

    def accesstree(self, root):
        if (root is not None):
            self.nodevalue.append(root.val)
            self.accesstree(root.left)
            self.accesstree(root.right)
        return self.nodevalue


r1 = TreeNode(1)
r1l = TreeNode(1)
r1r = TreeNode(1)
r1ll = TreeNode(1)
r1lr = TreeNode(1)
r1rr = TreeNode(1)
r1.left = r1l
r1.right = r1r
r1l.left = r1ll
r1l.right = r1rr
r1r.right = r1rr

s = Solution()
print(s.isUnivalTree(r1))
"""
此题解法：
* 使用前序遍历，先访问root，然后再访问左叶和右叶

"""
