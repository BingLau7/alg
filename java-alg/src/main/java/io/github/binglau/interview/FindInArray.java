package io.github.binglau.interview;

import java.util.Arrays;

/**
 * 类findInArray.java的实现描述：TODO:类实现描述
 *
 * 二维数组中的查找
 * 在一个二维数组重,每一行都按照从左到右递增的顺序排列,
 * 每一列都按照从上到下递增的顺序排序。请完成一个函数,
 * 输入这样的一个二维数组和一个整数,判断数组重是否含有该整数。
 * @author bingjian.lbj 2016-12-20 下午1:45
 */
public class FindInArray {

    public static boolean findInArray(int[][] array, int target) {
        int currentRow = -1;
        // 先检查第一排,判断这个数如果存在会在哪几列中
        for (int i = array.length; i > 0; i--) {
            if (array[0][i] < target) {
                currentRow = i;
                break;
            }
        }
        if (currentRow == -1) return false;
        // 挑选最大的那一列,从上到下判断,可以排除行数, 如果出现小于的数,则target不存在
        while (currentRow >= 0) {
            for (int j = 0; j < array[currentRow].length; j++) {
                if (array[currentRow][j] == target) return true;
                // 如果出现大于的数,则退后一排
                if (array[currentRow][j] > target) break;
                if (j == array[currentRow].length -1 && array[currentRow][j] < target) return false;
            }
            currentRow--;
        }
        // 如果最后都不符合,返回false
        return false;
    }

    public static void main(String[] args) {
        int[][] array = {{1, 4, 5, 7, 10}, {3, 6, 9, 12, 14}, {6, 8, 11, 14, 19}, {9, 13, 15, 21, 26}};
        System.out.println(findInArray(array, 8));
    }

}
