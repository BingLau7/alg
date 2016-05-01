#coding:utf-8
"""
    红黑树
"""
RED = 1
BLACK = 0

class Node(object):
    """
        红黑树结点
    """
    def __init__(self, key, left, right, parent):
        self.key = key
        self.color = BLACK
        self.left = left
        self.right = right
        self.parent = parent

    def change_color(self):
        """
            改变结点颜色
        """
        if self.color == RED:
            self.color = BLACK
        else:
            self.color = RED

    def get_value(self):
        """
            返回key对应的值，暂时无
        """
        return self.key

class RedBlackTree(object):
    """
        红黑树
    """
    NIL = Node(key=-1, left=None, right=None, parent=None)   #哨兵值
    NIL.color = BLACK

    def __init__(self, key):
        self._root = Node(key=key, left=RedBlackTree.NIL, right=RedBlackTree.NIL,\
                parent=RedBlackTree.NIL)
        self._height = 0

    def get_root(self):
        """
            返回树根
        """
        return self._root

    def left_rotate(self, node):
        """
            左旋转：对于树修改操作的修正，保持红黑性质
            将node向左旋转，使其左孩子成为node的父结点,
            而node成为原右孩子的左结点
        """
        right_child = node.right
        node.right = right_child.left

        if right_child.left != RedBlackTree.NIL:
            right_child.left.parent = node
        right_child.parent = node.parent

        if node.parent == RedBlackTree.NIL:
            self._root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        """
            右旋转:与左旋转对称
        """
        left_child = node.left
        node.left = left_child.right

        if left_child.right != RedBlackTree.NIL:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent == RedBlackTree.NIL:
            self._root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child

        left_child.right = node
        node.parent = left_child

    def rb_insert(self, key):
        """
            插入操作
        """
        node_y = RedBlackTree.NIL
        node_x = self._root
        while node_x != RedBlackTree.NIL:
            node_y = node_x
            if key < node_x.key:
                node_x = node_x.left
            elif key > node_x.key:
                node_x = node_x.right
            else:
                print '有重复'
                return
        new_node = Node(key=key, left=RedBlackTree.NIL, right=RedBlackTree.NIL,\
                parent=node_y)
        if node_y == RedBlackTree.NIL:
            self._root = new_node
        elif key < node_y.key:
            node_y.left = new_node
        else:
            node_y.right = new_node

        new_node.left = RedBlackTree.NIL
        new_node.right = RedBlackTree.NIL
        new_node.color = RED
        self.rb_insert_fixup(new_node)

    def rb_insert_fixup(self, node):
        """
            插入函数辅助，对结点重新着色并旋转,针对插入的父结点是红色
        """
        while node.parent.color == RED:

            if node.parent == node.parent.parent.left:
                parent_right_borther = node.parent.parent.right

                if parent_right_borther.color == RED:   #将父结点及其兄弟结点变为黑色，再令自己等于其祖父结点
                    node.parent.color = BLACK
                    parent_right_borther.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent

                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)

            else:
                parent_left_borther = node.parent.parent.left
                if parent_left_borther.color == RED:
                    node.parent.color = BLACK
                    parent_left_borther.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent

                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)

            self._root.color = BLACK

    def rb_search(self, key):
        """
            查询
        """
        node = self._root
        while node != RedBlackTree.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return node

    def rb_delete(self, key):
        """
            删除
        """
        node = self.rb_search(key)
        node_y = node
        node_y_original_color = node_y.color
        node_x = RedBlackTree.NIL   #结点x代表的是要取代node的结点
        if node.left == RedBlackTree.NIL:
            node_x = node.right
            self.rb_transplant(node, node.right)

        elif node.right == RedBlackTree.NIL:
            node_x = node.left
            self.rb_transplant(node, node.left)

        else:
            # print 'debug', node_y.parent.key
            node_y = self.minimum(node.right)
            node_y_original_color = node.color
            node_x = node_y.right

            if node_y.parent == node:
                node_x.parent = node_y
            else:
                self.rb_transplant(node_y, node_y.right)
                node_y.right = node.right
                node_y.right.parent = node_y
            self.rb_transplant(node, node_y)
            node_y.left = node.left
            node_y.left.parent = node_y
            node_y.color = node.color

        if node_y_original_color == BLACK:
            self.rb_delete_fixup(node_x)

    def rb_delete_fixup(self, node):
        """
            修复删除结点可能导致红黑树性质被破坏的情况
        """
        while node != self._root and node.color == BLACK:
            if node == node.parent.left:
                right_borther = node.parent.right

                if right_borther.color == RED:
                    right_borther = BLACK
                    node.parent.color = RED
                    self.left_rotate(node.parent)
                    right_borther = node.parent.right

                if right_borther.left.color == BLACK and right_borther.right.color == BLACK:
                    right_borther.color = RED
                    node = node.parent

                elif right_borther.right.color == BLACK:
                    right_borther.left.color = BLACK
                    right_borther.color = RED
                    self.right_rotate(right_borther)
                    right_borther = node.parent.right

                right_borther.color = node.parent.color
                node.parent.color = BLACK
                right_borther.right.color = BLACK
                self.left_rotate(node.parent)
                node = self._root

            else:
                left_borther = node.parent.left

                if left_borther.color == RED:
                    left_borther = BLACK
                    node.parent.color = RED
                    self.left_rotate(node.parent)
                    left_borther = node.parent.left

                if left_borther.right.color == BLACK and left_borther.left.color == BLACK:
                    left_borther.color = RED
                    node = node.parent

                elif left_borther.left.color == BLACK:
                    left_borther.right.color = BLACK
                    left_borther.color = RED
                    self.right_rotate(left_borther)
                    left_borther = node.parent.left

                left_borther.color = node.parent.color
                node.parent.color = BLACK
                left_borther.left.color = BLACK
                self.left_rotate(node.parent)
                node = self._root


    def rb_transplant(self, node_u, node_v):
        """
            使用node_v代替node_u,并没有处理node_u,v的左右孩子
        """
        if node_u.parent == RedBlackTree.NIL:
            self._root = node_v

        elif node_u == node_u.parent.left:
            node_u.parent.left = node_v

        else:
            node_u.parent.right = node_v

        node_v.parent = node_u.parent

    def minimum(self, node=None):
        """
            得到结点最小值
        """
        if not node:
            node = self._root

        # print 'debug', self._root.right.parent.key
        while node.left != RedBlackTree.NIL:
            node = node.left

        return node

    def priority_traverse(self, root):
        """
            中序遍历
        """
        if root == RedBlackTree.NIL:
            return
        print root.key
        self.priority_traverse(root.left)
        self.priority_traverse(root.right)

    def postorder_traverse(self, root):
        """
            后序遍历:左->右->中
        """
        if root == RedBlackTree.NIL:
            return
        self.postorder_traverse(root.left)
        self.postorder_traverse(root.right)
        print root.key


    def inorder_traverse(self, root):
        """
            中序遍历:左->中->右
        """
        if root == RedBlackTree.NIL:
            return
        self.inorder_traverse(root.left)
        print root.key
        self.inorder_traverse(root.right)



def test():
    """
        test function
    """
    tree = RedBlackTree(11)
    tree.rb_insert(2)
    tree.rb_insert(7)
    tree.rb_insert(1)
    tree.rb_insert(5)
    tree.rb_insert(8)
    tree.rb_insert(14)
    tree.rb_insert(15)
    tree.rb_insert(4)
    tree.inorder_traverse(tree.get_root())
    tree.rb_delete(11)
    # print tree.get_root().key
    tree.inorder_traverse(tree.get_root())


if __name__ == '__main__':
    test()
