/*
八皇后
*/

object Solution {
    // result[i] 表示把第i个皇后放在第i行的列数
    def queueN(n: Int): Array[Int] = {
        if (isConflict(Array(), n)) {
            Array(1, 2)
        }        
        
        Array(2, 3)
    }

    def isConflict(result: Array[Int], n: Int): Boolean = {
        for (i <- 1 to n) {
        }
        false
    }
}

println(Solution.queueN(1).deep.mkString("\n"))