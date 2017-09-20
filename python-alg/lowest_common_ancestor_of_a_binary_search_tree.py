#encoding:utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.result = []
        if not root:
            return

        if self.isChildren(p, q):
            return p
        elif self.isChildren(q, p):
            return q
        else:
            self.test(root, p, q)

        if self.result:
            return self.result[-1]
        return root




    def test(self, root, p, q):

        if self.isChildren(root.left, p) and self.isChildren(root.left, q):
            self.result.append(root.left)
            self.test(root.left, p, q)
        elif self.isChildren(root.right, p) and self.isChildren(root.right, q):
            self.result.append(root.right)
            self.test(root.right, p, q)


    def isChildren(self, p, q):
        """
          p是否是q的父节点
        """
        if not p or not q:
            return False
        if not p.left and not p.right:
            return False

        if p.left and p.left.val != q.val:
            if self.isChildren(p.left, q):
                return True
        elif p.left:
            return True

        if p.right and p.right.val != q.val:
            if self.isChildren(p.right, q):
                return True
        elif p.right:
            return True

        return False

if __name__ == '__main__':

    root = TreeNode(4)

    root.left  = TreeNode(2)
    t2 = TreeNode(7)
    root.right = t2

    t6 = TreeNode(1)
    root.left.right = t6

    # t3 = TreeNode(1)
    # root.left.left = t3
    # t3.left = TreeNode(11)
    # t4 = TreeNode(12)
    # t3.right = t4
    # t5 = TreeNode(3)
    # root.left.right = t5

    # t1 = TreeNode(6)

    # root.right.left = t1
    # root.right.right = TreeNode(9)

    print Solution().isChildren(root.left, t2)

    result = Solution().lowestCommonAncestor(root, t2, t6)
    print result.val

