package io.github.binglau.interview;

/**
 * 类FindMinInRotaryArray.java
 *
 * 在旋转数组中寻找最小的数，剑指offer面试题8
 *
 * @author bingjian.lbj 2017-01-15 下午9:14
 */
public class FindMinInRotaryArray {

    private static int findMinInOrder(int[] rotaryArray) {
        int min = rotaryArray[0];
        for (int i : rotaryArray) {
            if (i < min) min = i;
        }
        return min;
    }

    public static int findMinInRotaryArray(int[] rotaryArray) {
        if (rotaryArray == null || rotaryArray.length == 0) {
            throw new RuntimeException("Error");
        }

        // 指定两个指针，一个最左一个最右
        int i = 0;
        int j = rotaryArray.length - 1;
        int mid = i;
        // 因为i只能出现在j前，所以旋转数组若是出现rotaryArray[i] < rotaryArray[j]则证明该数组为顺序
        while (rotaryArray[i] >= rotaryArray[j]) {
            if (j - i == 1) {
                mid = j;
                break;
            }
            mid = (j + i) / 2;

            if (rotaryArray[i]  == rotaryArray[j] && rotaryArray[i] == rotaryArray[mid])
                return findMinInOrder(rotaryArray);

            if (rotaryArray[mid] >= rotaryArray[i]) { // 证明mid属于左边的递增数组
                i = mid;
            } else if (rotaryArray[mid] <= rotaryArray[j]) { // 证明mid属于右边的递增数组
                j = mid;
            }
        }
        return rotaryArray[mid];
    }

    public static void main(String[] args) {
        System.out.println(findMinInRotaryArray(new int[]{3, 4, 5, 1, 2}));
        System.out.println(findMinInRotaryArray(new int[]{1, 1, 1, 0, 1}));
    }
}
