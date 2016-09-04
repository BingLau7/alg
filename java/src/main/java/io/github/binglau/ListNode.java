package io.github.binglau;

import java.util.List;

/**
 * 类ListNode.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-08-29 下午7:00
 */
public class ListNode implements Cloneable{
    int val;
    ListNode next;
    ListNode(int x) { val = x; }

    public static ListNode create(int[] data) {
        if (data.length == 0){
            return null;
        }
        ListNode head = new ListNode(data[0]);
        if (data.length == 2) {
            return head;
        }
        for (int i = 1; i < data.length; i++) {
            add(head, data[i]);
        }
        return head;
    }

    public static void add(ListNode head, int data) {
        if (head == null) {
            head = new ListNode(data);
            return;
        }
        ListNode t = head;
        while (t.next != null) {
            t = t.next;
        }
        t.next = new ListNode(data);
    }

    public static void print(ListNode head) {
        ListNode t = head;
        while (t != null) {
            System.out.print("->" + t.val);
            t = t.next;
        }
        System.out.println();
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        Object ohead = super.clone();
        ListNode head = null;
        if (!(ohead instanceof ListNode)) {
            throw new Error("Class error");
        } else {
            head = (ListNode)ohead;
        }
        ListNode cloneHead = new ListNode(head.val);
        ListNode ct = cloneHead;
        ListNode t = head.next;
        while (t != null) {
            ct.next = new ListNode(t.val);
            t = t.next;
            ct = ct.next;
        }
        return cloneHead;
    }
}
