package io.github.binglau.list;

/**
 * 文件描述:
 * https://leetcode.com/problems/reverse-nodes-in-k-group/#/description
 *
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

 k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

 You may not alter the values in the nodes, only nodes itself may be changed.

 Only constant memory is allowed.

 For example,
 Given this linked list: 1->2->3->4->5

 For k = 2, you should return: 2->1->4->3->5

 For k = 3, you should return: 3->2->1->4->5
 */

public class ReverseNodesInKGroup {
    public static ListNode reverseKGroup(ListNode head, int k) {
        if (k <= 1) return head;
        if (head == null || head.next == null) return head;

        int listLen = 0;
        ListNode c = head;
        while (c != null) {
            c = c.next;
            listLen++;
        }
        if (k > listLen) return head;

        ListNode p = head;
        ListNode q = head.next;

        ListNode r = q.next;

        // 反转的思路
        p.next = null;
        while (r != null && k > 2) {
            ListNode t = q;
            q.next = p;
            p = t;
            q = r;
            r = q.next;
            k--;
        }

        // 保存 k 次反转后面的链表
        ListNode tt = q.next;
        q.next = p;
        ListNode cur = q;
        // 在反转后的链表尾部插入未反转的链表
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = tt;

        return q;
    }

    public static void main(String[] args) {
        ListNode head1 = ListNode.create(new int[]{1, 2, 3, 4, 5});
        ListNode.print(reverseKGroup(head1,2));
    }
}
