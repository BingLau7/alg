package io.github.binglau.list;

/**
 * 类ReverseList.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-04 下午6:26
 */
public class ReverseList {
    public static ListNode reverseList(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode p = head;
        ListNode q = head.next;
        ListNode r = q.next;
        p.next = null;
        while (r != null) {
            ListNode t = q;
            q.next = p;
            p = t;
            q = r;
            r = q.next;
        }
        q.next = p;
        return q;
    }

    public static void main(String[] args) {
        ListNode head = ListNode.create(new int[]{1, 2, 4, 12, 33});
        ListNode.print(head);
        ListNode rhead = reverseList(head);
        ListNode.print(rhead);
    }
}
