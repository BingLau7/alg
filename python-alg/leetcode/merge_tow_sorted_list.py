# coding=utf-8

"""文件描述

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from leetcode.list_node import ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 边界判断
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        # 锁定顺序
        left, right = l1, l2
        if left.val > right.val:
            left, right = right, left

        root = left
        # 边界判断
        if not left.next:
            left.next = right
            return root

        while left.next and right:
            if left.next.val > right.val:
                tmp = left.next
                left.next = ListNode(right.val)
                left.next.next = tmp
                right = right.next
            left = left.next
        while left.next:
            left = left.next
        if right:
            left.next = right
        return root


if __name__ == '__main__':
    print(Solution().mergeTwoLists(ListNode.create([1, 2, 4]), ListNode.create([1, 3, 4])).string())
