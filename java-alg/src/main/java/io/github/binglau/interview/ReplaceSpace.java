package io.github.binglau.interview;

/**
 * 类ReplaceSpace.java的实现描述：TODO:类实现描述
 *
 * 替换空格
 *
 * 请实现一个函数,把字符串中的每个空格替换成"%20",
 * 例如输入"We are happy.",则输出 "We%20are%20happy."。
 *
 * @author bingjian.lbj 2016-12-23 上午12:04
 */
public class ReplaceSpace {

    public static String replaceSpace(String srcString){
        String result = srcString.replace(" ", "%20");
        return result;
    }

    public static void main(String[] args) {
        System.out.println(replaceSpace("We are happy."));
    }
}
