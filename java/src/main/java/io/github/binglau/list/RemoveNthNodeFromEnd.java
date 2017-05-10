package io.github.binglau.list;

/**
 *  https://leetcode.com/problems/remove-nth-node-from-end-of-list/#/description
 *
 Given a linked list, remove the nth node from the end of list and return its head.

 For example,

 Given linked list: 1->2->3->4->5, and n = 2.

 After removing the second node from the end, the linked list becomes 1->2->3->5.
 Note:
 Given n will always be valid.
 Try to do this in one pass.
 */
public class RemoveNthNodeFromEnd {
    public static ListNode removeNthFromEnd(ListNode head, int n) {
        // 删除的既是根节点也是最后一个节点
        if (n==1 && head.next == null) return null;
        ListNode hi = head, lo = head;
        for (int i = 0; i < n - 1; i++) {
            hi = hi.next;
        }
        // 删除了根节点, hi通过 n 步跑到了节点末尾证明 n + 1 是链表长
        if (hi.next == null) return head.next;
        // lo 是要删除的节点的之前的节点
        while (hi.next.next != null) {
            lo = lo.next;
            hi = hi.next;
        }
        lo.next = lo.next.next;
        return head;
    }

    public static void main(String[] args) {
        ListNode head = ListNode.create(new int[]{1, 2, 3, 4, 5});
        ListNode r = removeNthFromEnd(head, 1);
        ListNode.print(r);
    }
}
