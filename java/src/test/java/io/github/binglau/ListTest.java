package io.github.binglau;

import org.junit.Test;

/**
 * 类ListTest.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-08-29 下午7:06
 */
public class ListTest {
    @Test
    public void testCreate(){
        ListNode head = ListNode.create(new int[]{1, 2, 3, 4, 5});
        ListNode.print(head);
    }

    @Test
    public void testClone() throws CloneNotSupportedException{
        ListNode head = ListNode.create(new int[]{1, 2, 3, 4, 5});
        ListNode cHead = (ListNode)head.clone();
        ListNode.print(head);
        ListNode.print(cHead);
    }

    @Test
    public void testOddEventLinkedList(){
        ListNode head = ListNode.create(new int[]{1, 2, 3, 4, 5});
        new OddEvenLinkedList().oddEvenList(head);
        ListNode.print(head);
    }

    @Test
    public void testPalindromeLinkedList() {
        ListNode head = ListNode.create(new int[]{1, 2, 3, 4, 5});
        new PalindromeLinkedList().isPalindrome(head);
    }
}
