# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if (root is None):
            return self.result
        stack = []
        current = root

        while (len(stack) != 0 or current is not None):
            if (current is not None):
                stack.append(current)
                current = current.left
            else:
                top = stack.pop()
                self.result.append(top.val)
                current = top.right
        return self.result

    def inorderTraversalRecursion(self, root):
        if (root is not None):
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)
        return self.result


root = TreeNode(1)
l1 = TreeNode(2)
r = TreeNode(3)
ll = TreeNode(3)
lr = TreeNode(4)
rl = TreeNode(4)
rr = TreeNode(2)

root.left = l1
root.right = r
l1.left = ll
r.left = rr

s = Solution()
ret = s.inorderTraversal(root)
print(ret)

s.result.clear()
ret1 = s.inorderTraversalRecursion(root)
print(ret1)
"""
中序遍历：先遍历左子树，然后访问根节点，最后遍历右子树。

递归版本

class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):

        if (root is not None):
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)

"""
