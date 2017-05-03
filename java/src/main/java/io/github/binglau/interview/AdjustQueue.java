package io.github.binglau.interview;

/**
 * https://mp.weixin.qq.com/s?__biz=MzI1MTIzMzI2MA==&mid=2650560958&idx=2&sn=81b4afe048b81468d5aa8913f45cf064&chksm=f1feef3dc689662b7e14a5bf2c7e6580bc84944eedcbd7aaaf7109e667bfd40a02ad6531b905&scene=0&key=62055592bb8cb96beeed75e00b25dbc3e1ad759958d25ceb224ce7a0cf01d1775b98ec4431043a47d3a28e098f1289fb84ca80b7db9a524449d31638c137b4f5796021e6cb930aba6688d95af55dcc44&ascene=0&uin=MjEyNTA1NTIyMQ%3D%3D&devicetype=iMac+MacBookPro12%2C1+OSX+OSX+10.12.4+build(16E195)&version=12020510&nettype=WIFI&fontScale=100&pass_ticket=dE%2Ba6Cy3v3tDCKKa0DHnJYlazrYXoNM5EbVXGcas3EaaBfVmr40lXOucMghhBYzU
 *
 在幼儿园有n个小朋友排列为一个队伍，从左到右一个挨着一个编号为(0~n-1)。
 其中有一些是男生，有一些是女生，男生用’B’表示，女生用’G’表示。
 小朋友们都很顽皮，当一个男生挨着的是女生的时候就会发生矛盾。

 作为幼儿园的老师，你需要让男生挨着女生或者女生挨着男生的情况最少。
 你只能在原队形上进行调整，每次调整只能让相邻的两个小朋友交换位置，
 现在需要尽快完成队伍调整，你需要计算出最少需要调整多少次可以让上述情况最少。例如：

 GGBBG -> GGBGB -> GGGBB

 这样就使之前的两处男女相邻变为一处相邻，需要调整队形2次

 输入描述: 输入数据包括一个长度为n且只包含G和B的字符串.n不超过50.

 输出描述: 输出一个整数，表示最少需要的调整队伍的次数

 输入例子: GGBBG

 输出例子: 2


 */
public class AdjustQueue {

    // 思路：左右一个指针做交换
    private static int adjustQueue(String s) {
        return Math.min(adjustQueue(s, 'G'), adjustQueue(s, 'B'));
    }

    private static int adjustQueue(String s, char f) {
        char h;
        if (f == 'G') h = 'B';
        else h = 'G';
        int result = 0;
        for (int i = 0, j = s.length() - 1; i < s.length() && j > 0 && i != j;) {
            if (s.charAt(i) == f && s.charAt(j) == h) {
                result++;
                i++;
                j--;
            }
            if (s.charAt(i) != f) i++;
            if (s.charAt(j) != h) j--;
        }
        return result;
    }


    public static void main(String[] args) {
        System.out.println(adjustQueue("GGGBB"));
    }
}
