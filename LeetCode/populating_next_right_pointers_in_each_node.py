#!/usr/bin/env python
# encoding: utf-8

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
            有点像层序遍历
        """
        if root is None:
            return

        levels = [[root]]
        self.level_connect(levels)

    def level_connect(self, levels):
        while levels:
            level = levels.pop(0)
            new_level = []
            while level:
                node = level.pop(0)
                if len(level):
                    node.next = level[0]
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if new_level:
                levels.append(new_level)
