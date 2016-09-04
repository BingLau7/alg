package io.github.binglau;

import java.util.ArrayList;
import java.util.List;

/**
 * 类PalindromeLinkedList.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-04 下午6:17
 */
public class PalindromeLinkedList {
    public boolean isPalindrome(ListNode head){
        ListNode t = head;
        List<Integer> h = new ArrayList<>();
        while (t != null) {
            h.add(t.val);
            t = t.next;
        }
        int i = 0;
        int j = h.size() - 1;
        while (j > i) {
            if (!h.get(i).equals(h.get(j))){
                return false;
            }
            j--; i++;
        }
        return true;
    }
}
