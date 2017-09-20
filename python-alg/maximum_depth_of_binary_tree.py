#!/usr/bin/env python
# encoding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        """
            最大深度的最优子结构是以它的下一级子树为根也是最大深度
            max_depth(root) = max(max_depth(root.left), max_depth(root.right)) + 1
            当root为叶子结点则为0
            有两个情况：
                1. 没有左子树，则max_depth(root) = max(max_depth(root.right)) + 1
                2. 没有右子树，则max_depth(root) = max(max_depth(root.left)) + 1
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return self.maxDepth(root.right) + 1
        elif root.right == None:
            return self.maxDepth(root.left) + 1
        else:
            max_depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            return max_depth

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.left.right = TreeNode(2)
    print Solution().maxDepth(root)
