"""

https://leetcode.com/problems/swap-nodes-in-pairs/description/

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the
values in the list, only nodes itself can be changed.

"""
from leetcode.list_node import ListNode


def swapPairs(head):
    pass

def swap(a, b, c):
    # 不可能出现 a 和 c 都是 None 的情况
    assert b is not None
    assert a is not None or c is not None
    if c is None: # tail 单数交换情况，不执行交换
        return
    # head 头的情况
    if a:
        a.next = c
    if c:
        b.next = c.next
        c.next = b


def main():
    print("测试")
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    # swap(None, a, b) # 期待 a, b 换
    # print(b.val, b.next.val, b.next.next.val)
    # swap(b, c, None) # 期待 不换
    # print(b.val, b.next.val, b.next.next is None)
    # swap(a, b, c) # 期待 b, c 换
    # print(a.val, a.next.val, a.next.next.val)

if __name__ == '__main__':
    main()
