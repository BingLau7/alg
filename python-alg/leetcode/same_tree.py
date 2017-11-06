#!/usr/bin/env python
# encoding: utf-8

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        """
            两个树是否相等取决于它们值是否相等，
            如果两个树相等则它们的左子树和右子树也一定相等
            isSameTree(p, q) = isSameTree(p.left, q.left) and isSameTree(p.right, q.right) and p.val == q.val
            叶子情况:
                isSameTree(p, q) = p.val == q.val
            无左子树结点：
                isSameTree(p, q) = isSameTree(p.right, q.right) and p.val == q.val
            无右子树结点：
                isSameTree(p, q) = isSameTree(p.left, q.left) and p.val == q.val
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.left == None and p.left == None and q.left == None and q.right == None:  #叶子情况
            return p.val == q.val
        elif p.left == None and q.left == None:
            return self.isSameTree(p.right, q.right) and p.val == q.val
        elif q.right == None and q.right == None:
            return self.isSameTree(p.left, q.left) and p.val == q.val
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val
