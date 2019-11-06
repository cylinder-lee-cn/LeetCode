# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def postorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if (root is not None):
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)
            self.result.append(root.val)
        return self.result

    def postorderTraversal(self, root):
        if (root is None):
            return self.result

        stack1 = []
        stack2 = []
        stack1.append(root)

        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if (current.left is not None):
                stack1.append(current.left)
            if (current.right is not None):
                stack1.append(current.right)

        while stack2:
            self.result.append(stack2.pop().val)

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
ret = s.postorderTraversal(root)
print(ret)

s.result.clear()
ret1 = s.postorderTraversalRecursion(root)
print(ret1)
