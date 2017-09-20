package io.github.binglau.programming_pearls;

public class IBit {
    private static final int WORK_SPACE = 32;
    private static final int MARK = 0x1f;
    private static final int SHIFT = 5; // 因为WORK_SPACE为32
    int[] a = null;

    public IBit(int n) {
        a = new int[1 + n / WORK_SPACE];
    }

    public void set(int i) {
        a[i>>SHIFT] |= (1<<(i & MARK));
    }

    public void clr(int i) {
        a[i>>SHIFT] &= ~(1<<(i & MARK));
    }

    public int test(int i) {
        return a[i>>SHIFT] & (1<<(i & MARK));
    }

    public static void main(String[] args) {
        IBit iBit = new IBit(200);
        iBit.set(10);
        System.out.println();
    }
}
