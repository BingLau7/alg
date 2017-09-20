package io.github.binglau.unkown;

import io.github.binglau.list.ListNode;

/**
 * https://leetcode.com/problems/add-two-numbers/#/description
 *
 You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

 You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output: 7 -> 0 -> 8
 */
public class AddTwoNumbers {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result;
        if (l1 == null || l2 == null) return null;

        // 第一次初始化 result 需要提出来
        int res = l1.val + l2.val;
        if (res >= 10) {
            result = new ListNode(res-10);
            carryOver(l1, l2, result);
        } else {
            result = new ListNode(res);
        }

        l1 = l1.next;
        l2 = l2.next;

        ListNode rtmp = result;

        // 先同进退
        while (l1 != null && l2 != null) {
            int tmp = l1.val + l2.val;
            if (tmp >= 10) {
                rtmp.next = new ListNode(tmp-10);
                carryOver(l1, l2, rtmp.next);
            } else {
                rtmp.next = new ListNode(tmp);
            }
            rtmp = rtmp.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        // 查看 l1 or l2 哪个没有完成
        if (l1 != null) {
            rtmp.next = l1;
        } else if (l2 != null) {
            rtmp.next = l2;
        }

        return result;
    }

    private static void carryOver(ListNode l1, ListNode l2, ListNode result) {
        if (l1.next != null) carryOver(l1);
        else if (l2.next != null) carryOver(l2);
        else result.next = new ListNode(1);
    }

    private static void carryOver(ListNode l) {
        if (l.next == null) {
            l.next = new ListNode(1);
        } else {
            l.next.val++;
            if (l.next.val == 10) {
                l.next.val = 0;
                carryOver(l.next);
            }
        }
    }

    private static ListNode answerSolution(ListNode l1, ListNode l2) {
        ListNode prev = new ListNode(0);
        ListNode head = prev;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            ListNode cur = new ListNode(0);
            int sum = ((l2 == null) ? 0 : l2.val) + ((l1 == null) ? 0 : l1.val) + carry;
            cur.val = sum % 10;
            carry = sum / 10;
            prev.next = cur;
            prev = cur;

            l1 = (l1 == null) ? l1 : l1.next;
            l2 = (l2 == null) ? l2 : l2.next;
        }
        return head.next;
    }


    public static void main(String[] args) {
        ListNode l1 = ListNode.create(new int[]{1});
        ListNode l2 = ListNode.create(new int[]{9, 9});
        ListNode.print(addTwoNumbers(l1, l2));
    }
}
