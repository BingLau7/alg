package io.github.binglau.unkown;

import io.github.binglau.list.ListNode;

import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * 文件描述:
 * https://leetcode.com/problems/merge-k-sorted-lists/#/description
 * Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
 */

public class MergeKSortedLists {
    public static ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;

        PriorityQueue<ListNode> queue = new PriorityQueue<>(lists.length, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                if (o1.val < o2.val) return -1;
                else if (o1.val == o2.val) return 0;
                else return 1;
            }
        });

        ListNode head = new ListNode(0);
        ListNode tail = head;

        for (ListNode node : lists) {
            if (node != null) queue.add(node);
        }

        while (!queue.isEmpty()) {
            tail.next = queue.poll();
            tail = tail.next;

            if (tail.next != null) queue.add(tail.next);
        }

        return head.next;
    }

    public static void main(String[] args) {
        ListNode head1 = ListNode.create(new int[]{5, 6, 11});
        ListNode head2 = ListNode.create(new int[]{1, 8, 14});
        ListNode head3 = ListNode.create(new int[]{12, 19});
        ListNode.print(mergeKLists(new ListNode[]{head1, head2, head3}));
    }
}
