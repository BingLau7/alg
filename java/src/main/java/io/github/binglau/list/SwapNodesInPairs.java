package io.github.binglau.list;

/**
 * 文件描述:
 * https://leetcode.com/problems/swap-nodes-in-pairs/#/description
 *
 Given a linked list, swap every two adjacent nodes and return its head.

 For example,
 Given 1->2->3->4, you should return the list as 2->1->4->3.

 Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
 */
public class SwapNodesInPairs {
    public static ListNode swapPairs(ListNode head) {
        ListNode tmp = null;
        ListNode cur = head;

        if (head == null) return null;

        while (cur.next != null) {
            if (tmp == null) tmp = cur;
            else { // tmp 的值和 cur 交换
                int v = cur.val;
                cur.val = tmp.val;
                tmp.val = v;
                tmp = null;
            }
            cur = cur.next;
        }

        if (tmp != null) {
            int v = cur.val;
            cur.val = tmp.val;
            tmp.val = v;
        }
        return head;
    }

    public static void main(String[] args) {
        ListNode head1 = ListNode.create(new int[]{5, 6, 11, 12});
        ListNode.print(swapPairs(head1));
    }
}
