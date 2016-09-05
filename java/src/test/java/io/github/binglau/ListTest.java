package io.github.binglau;

import io.github.binglau.list.IntersectionOfTowLinkedList;
import io.github.binglau.list.ListNode;
import io.github.binglau.list.OddEvenLinkedList;
import io.github.binglau.list.PalindromeLinkedList;
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
    public void testRemove() {
        ListNode head = ListNode.create(new int[]{1, 2, 3});
        ListNode.print(head);
        ListNode t = ListNode.remove(head, 3);
        ListNode.print(t);
    }

    @Test
    public void testOddEventLinkedList(){
        ListNode head = ListNode.create(new int[]{1, 2, 3, 4, 5});
        new OddEvenLinkedList().oddEvenList(head);
        ListNode.print(head);
    }

    @Test
    public void testPalindromeLinkedList() {
        ListNode head = ListNode.create(new int[]{5, 4, 3, 4, 5});
        boolean result = new PalindromeLinkedList().isPalindrome(head);
        System.out.println(result);
    }

    @Test
    public void testIntersectionOfTwoLinkedList() {
        ListNode aHead = ListNode.create(new int[]{1, 2});
        ListNode bHead = ListNode.create(new int[]{3, 4, 5});
        ListNode cHead = ListNode.create(new int[]{7, 2, 3, 4, 5});
        ListNode aT = aHead;
        ListNode bT = bHead;
        while (aT.next != null) aT = aT.next;
        while (bT.next != null) bT = bT.next;
        aT.next= cHead;
        bT.next = cHead;
        ListNode.print(aHead);
        ListNode.print(bHead);

//        ListNode r = new IntersectionOfTowLinkedList().getIntersectionNodeByHashSet(aHead, bHead);
        ListNode r = new IntersectionOfTowLinkedList().getIntersectionNodeByDiffLen(aHead, bHead);
        System.out.println(r.val);
    }
}
