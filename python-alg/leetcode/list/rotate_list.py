from list.node import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        # get tail and len
        tail = head
        _len = 0
        tmp_for_tail = head
        while tmp_for_tail:
            if tmp_for_tail.next is None:
                tail = tmp_for_tail
            tmp_for_tail = tmp_for_tail.next
            _len += 1

        # 找到新的 head
        new_head = head
        adv = _len - (k % _len)
        for i in range(adv):
            new_head = new_head.next
            if not new_head:  # 循环场景
                new_head = head

        # 找出 new_head 之前的点，并将其置为新的 tail
        tmp = head
        if tmp == new_head:
            return new_head
        while tmp:
            if tmp.next == new_head:
                tmp.next = None
                break
            tmp = tmp.next
        tail.next = head
        return new_head


if __name__ == '__main__':
    # head = ListNode.create(1, 2)
    # head = ListNode.create(1, 2, 3, 4, 5)
    head = ListNode.create(0, 1, 2)
    print(ListNode.toArray(Solution().rotateRight(head, 4)))
