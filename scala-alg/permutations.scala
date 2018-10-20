import scala.collection._

/*
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
*/

object Solution {
    def permute(nums: Array[Int]): List[List[Int]] = {
        def permute(rem: Set[Int]): Set[List[Int]] = {
            println(s"rem: $rem")
            if (rem.isEmpty) Set(Nil) // Nil 代指 List()
            else for (n <- rem; p <- permute(rem - n)) yield {
                println(s"n: $n, p: $p")
                n :: p
            }
        }
        println(nums.toSet)
        permute(nums.toSet).toList
    }
}

println(Solution.permute(Array(1, 2, 3)))