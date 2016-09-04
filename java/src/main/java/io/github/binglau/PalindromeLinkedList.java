package io.github.binglau;

/**
 * 类PalindromeLinkedList.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-04 下午6:17
 */
public class PalindromeLinkedList {
    public boolean isPalindrome(ListNode head) {
        // clone ListNode
        // 逆转链表
        ListNode reHead = new ReverseList().reverseList(head);
        ListNode.print(reHead);
        ListNode.print(head);
        return false;
    }
}
