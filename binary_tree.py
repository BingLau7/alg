#coding:utf-8
"""
    构造二叉树
"""
class BinaryTree(object):
    """
        二叉树
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def priority_traverse(self, root):
        """
            先序遍历：中->左->右
        """
        if not root:
            return
        print root.key
        self.priority_traverse(root.left)
        self.priority_traverse(root.right)

    def postorder_traverse(self, root):
        """
            后序遍历:左->右->中
        """
        if not root:
            return
        self.postorder_traverse(root.left)
        self.postorder_traverse(root.right)
        print root.key


    def inorder_traverse(self, root):
        """
            中序遍历:左->中->右
        """
        if not root:
            return
        self.inorder_traverse(root.left)
        print root.key
        self.inorder_traverse(root.right)

def insert_left(parent, key):
    """
        向树中插入一个结点
    """
    if not parent.left:
        parent.left = BinaryTree(key)
    else:
        tmp = BinaryTree(key)
        tmp.left = parent.left
        parent.left = tmp
    return parent.left

def insert_right(parent, key):
    """
        向树中插入一个结点
    """
    if not parent.right:
        parent.right = BinaryTree(key)
    else:
        tmp = BinaryTree(key)
        tmp.right = parent.right
        parent.right = tmp
    return parent.right

def delete_left(parent):
    """
        删除树中的左子树的结点
    """
    tmp = parent.left
    while not tmp:
        tmp = tmp.left
    parent.left = tmp
    tmp = None


def delete_right(parent):
    """
        删除树中的左子树的结点
    """
    tmp = parent.right
    while not tmp:
        tmp = tmp.right
    parent.right = tmp
    tmp = None

def test():
    """
        Test function
    """
    root = BinaryTree(2)
    tmp = insert_left(root, 3)
    insert_left(tmp, 1)
    tmp = insert_right(root, 4)
    insert_left(tmp, 5)
    delete_left(tmp)
    root.inorder_traverse(root)

if __name__ == '__main__':
    test()
