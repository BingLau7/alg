#encoding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.test(root)


    def test(self, root):
        tmp = root
        if tmp:
            if tmp.left or tmp.right:
                tmp.left, tmp.right = tmp.right, tmp.left
                if tmp.left:
                    self.test(tmp.left)
                if tmp.right:
                    self.test(tmp.right)


if __name__ == '__main__':
    root = TreeNode(4)

    root.left  = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)


    Solution().invertTree(root)

    print(root.left.val)
