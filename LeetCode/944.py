"""
944. 删除列以使之有序

给出由 N 个小写字母串组成的数组 A，所有小写字母串的长度都相同。
现在，我们可以选择任何一组删除索引，对于每个字符串，我们将删除这些索引中的所有字符。
举个例子，如果字符串为 "abcdef"，且删除索引是 {0, 2, 3}，那么删除之后的最终字符串为 "bef"。
假设我们选择了一组删除索引 D，在执行删除操作之后，A 中剩余的每一列都是有序的。
形式上，第 c 列为 [A[0][c], A[1][c], ..., A[A.length-1][c]]
返回 D.length 的最小可能值。


示例 1：
输入：["cba","daf","ghi"]
输出：1

示例 2：
输入：["a","b"]
输出：0

示例 3：
输入：["zyx","wvu","tsr"]
输出：3

提示：
1 <= A.length <= 100
1 <= A[i].length <= 1000
"""


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        B = zip(*A)

        for col in B:
            tmp = list(col)
            if (tmp != sorted(tmp) or tmp != sorted(tmp)):
                count = count + 1
        return count


"""
此题解法：
* 要求是这个数组A中的每一列都有序，比如：["cba","daf","ghi"]的每一列是 cdg,bah,afi
* 如果是有序那就是每一列要么是升序，要么是降序排列，如果无序这列就需要删除。
* 获取每一列是可以用zip(*A)，然后做排序的比较，如果无序就计数+1
"""
s = Solution()
print(s.minDeletionSize(["cba", "daf", "ghi"]))
print(s.minDeletionSize(["a", "b"]))
print(s.minDeletionSize(["zyx", "wvu", "tsr"]))
