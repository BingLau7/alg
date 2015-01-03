#coding:utf-8
"""
    二叉搜索树
"""
from random import shuffle

class TreeNode(object):
    """
        二叉查找树的结点
    """
    def __init__(self, key, left, right, parent):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = 0

    def get_key(self):
        """
            返回结点值
        """
        return self.key

    def set_key(self, key):
        """
            设置结点值
        """
        self.key = key

class BinarySearchTree(object):
    """
        二叉搜索树
    """
    def __init__(self, key):
        self._root = TreeNode(key=key, left=None, right=None, parent=None)
        self._height = 0

    def get_root(self):
        """
            返回树的根
        """
        return self._root

    def get_height(self):
        """
            返回树的高度
        """
        return self._height


    def insert(self, key):
        """
            二叉树插入
        """
        tmp = self._root
        node = None
        while tmp:
            node = tmp
            if key < node.key:
                tmp = tmp.left
            elif key > node.key:
                tmp = tmp.right
            else:
                print '有重复'
                return

        new_node = TreeNode(key=key, left=None, right=None, parent=node)
        if not node:
            self._root = new_node
        elif key < node.key:
            node.left = new_node
        else:
            node.right = new_node
        new_node.depth = node.depth + 1
        if new_node.depth > self._height:
            self._height += 1

    def search(self, key):
        """
            迭代实现
        """
        node = self._root
        while node and key != node.key:
            if key > node.key:
                node = node.right
            else:
                node = node.left

        return node

    def minimum(self, node=None):
        """
            迭代实现
        """
        if not node:
            node = self._root
        while node.left:
            node = node.left
        return node

    def maximum(self, node=None):
        """
            迭代实现
        """
        if not node:
            node = self._root
        while node.right:
            node = node.right
        return node

    def _transplant(self, subtree_u, subtree_v):
        """
            为了在二叉搜索树内移动子树。
            它是用另一棵子树替换一颗子树并成为其双亲的孩子结点。
            用v为根的子树来替换以u为根的子树，结点u的双亲就变成结点v的双亲，
            并且最后v成为u的双亲的对应孩子
            该函数并没有处理v.left和v.right的更新，这些更新都由_transplant的调用者来负责
        """
        if not subtree_u.parent:
            self._root = subtree_v
        elif subtree_u == subtree_u.parent.left:
            subtree_u.parent.left = subtree_v
        else:
            subtree_u.parent.right = subtree_v

        if subtree_v:
            subtree_v.parent = subtree_u.parent

    def delete(self, key):
        """
            删除
        """
        node = self.search(key)
        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            successor_node = self.minimum(node.right)
            if successor_node.parent != node:
                #后继非其右结点,先处理其后继结点，使其用后继结点的右孩子代替
                self._transplant(successor_node, successor_node.right)
                successor_node.right = node.right
                successor_node.left = successor_node.left
            #后继结点替换被删除结点
            self._transplant(node, successor_node)
            successor_node.left = node.left
            successor_node.left.parent = successor_node

    def get_successor(self, node):
        """
           得到node的后继(中序)
        """
        if node.right:
            return self.minimum(node.right)

        successor = node.parent
        while successor and node == successor.right:
            #如果node不是它父结点的右子树则后继是父结点
            #否则，就是祖父结点
            node, successor = successor, successor.parent
        return successor

    def get_predecessor(self, node):
        """
            得到前驱
        """
        if node.left:
            return self.minimum(node.left)

        predecessor = node.parent
        while predecessor and node == predecessor.left:
            node, predecessor = predecessor, predecessor.parent
        return predecessor

    def priority_traverse(self, root):
        """
            中序遍历
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

def create_tree_with_list(*keys):
    """
        输入keys为一组数，
        使用这组树搭建一颗二叉树,并返回
    """
    keys = list(keys)
    shuffle(keys)
    length_keys = len(keys)
    root_key = keys[0]
    tree = BinarySearchTree(root_key)
    for i in range(1, length_keys):
        tree.insert(keys[i])
    return tree

def test():
    """
        测试函数
    """
    tree = create_tree_with_list(12, 5, 2, 9, 18, 15, 13, 17, 19)
    tree.priority_traverse(tree.get_root())

if __name__ == '__main__':
    test()
