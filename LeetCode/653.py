"""
653. 两数之和 IV - 输入 BST


给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
输出: True


案例 2:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
输出: False
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if (root is None):
            return False

        d = set()
        stack = []
        stack.append(root)
        while (len(stack) != 0):
            top = stack.pop()
            if (top.val in d):
                return True
            else:
                d.add(k - top.val)

            if (top.right is not None):
                stack.append(top.right)
            if (top.left is not None):
                stack.append(top.left)
        return False


tn = TreeNode(5)
tnl = TreeNode(3)
tnr = TreeNode(6)
tnll = TreeNode(2)
tnlr = TreeNode(4)
tnrr = TreeNode(7)

tn.left = tnl
tn.right = tnr
tnl.left = tnll
tnlr.right = tnlr
tnr.right = tnrr

s = Solution()
print(s.findTarget(tn, 19))
"""
此题解法：
* 此题本质上与第1题一样，都是利用字典来完成
* 通过任意方法来遍历BTree，然后在字典中查找是否有key=k-treenode.val，如果存在，就返回True
* 反之，将k-treenode.val存入字典，如果遍历完都没发现，就返回False

"""
