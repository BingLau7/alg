#!/usr/bin/env python
# encoding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = []
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root is None:
            return self.result
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result
