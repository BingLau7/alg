#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
from .list_node import ListNode

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        """
            速度差来得到
        """
        if not head:
            return False
        p = head
        q = head

        while p and q:
            p = p.next
            if not q.next:
                return False
            q = q.next.next
            if p == q:
                return True
        return False


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    # head.next.next.next = head
    print(Solution().hasCycle(head))

