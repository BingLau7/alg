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
}
