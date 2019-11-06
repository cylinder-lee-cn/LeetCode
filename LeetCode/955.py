"""
955. 删列造序 ||

给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。

选取一个删除索引序列，对于 A 中的每个字符串，删除对应每个索引处的字符。

比如，有 A = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 A 为["bef", "vyz"]。

假设，我们选择了一组删除索引 D，那么在执行删除操作之后，最终得到的数组的元素是按
字典序（A[0] <= A[1] <= A[2] ... <= A[A.length - 1]）排列的，然后请你返回 D.length 的最小可能值。


示例 1：
输入：["ca","bb","ac"]
输出：1
解释：
删除第一列后，A = ["a", "b", "c"]。
现在 A 中元素是按字典排列的 (即，A[0] <= A[1] <= A[2])。
我们至少需要进行 1 次删除，因为最初 A 不是按字典序排列的，所以答案是 1。

示例 2：
输入：["xc","yb","za"]
输出：0
解释：
A 的列已经是按字典序排列了，所以我们不需要删除任何东西。
注意 A 的行不需要按字典序排列。
也就是说，A[0][0] <= A[0][1] <= ... 不一定成立。

示例 3：
输入：["zyx","wvu","tsr"]
输出：3
解释：
我们必须删掉每一列。

提示：
1 <= A.length <= 100
1 <= A[i].length <= 100
"""


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        cols = len(A[0])
        items = len(A)
        sortflag = [False] * (items - 1)  # 默认都是False，记录依次两个元素的排序关系

        count = 0  # 计数器

        for idx in range(cols):
            for j in range(items - 1):
                if sortflag[j] is False and A[j][idx] > A[j + 1][idx]:
                    count = count + 1
                    break
                    # 如果前一列的排序是False，而且此列还有逆序，计数器+1，利用else
                    # 来完成该列完整的排序比较并记录状态
            else:
                for j in range(items - 1):
                    if sortflag[j] is False and A[j][idx] < A[j + 1][idx]:
                        sortflag[j] = True
            # print(sortflag)
        return count


s = Solution()
# print(s.minDeletionSize(["ca", "bb", "ac"]))  # 1
# print(s.minDeletionSize(["xc", "yb", "za"]))  # 0
# print(s.minDeletionSize(["zyx", "wvu", "tsr"]))  # 3
# print(s.minDeletionSize(["abyx", "abvu", "atsr"]))  # 2
# print(s.minDeletionSize(["xga", "xfb", "yfa"]))  # 1
# print(s.minDeletionSize(["ousnatait", "xzswvwztr", "luknznxob"]))  # 4
# print(
#     s.minDeletionSize([
#         "bwwdyeyfhc", "bchpphbtkh", "hmpudwfkpw", "lqeoyqkqwe", "riobghmpaa",
#         "stbheblgao", "snlaewujlc", "tqlzolljas", "twdkexzvfx", "wacnnhjdis"
#     ]))  # 4
print(s.minDeletionSize(["koccmoezl", "hbccayhbd"]))  # 3
# print(
#     s.minDeletionSize([
#         "voibobzhfx", "qpabpzscga", "bjobaztasc", "lnbcakfmnq", "tjsikfdsix",
#         "dloiskwypl", "eaeqmujszw", "utfrgwyijs", "rxgyhhladh", "rmryzonepz"
#     ]))  # 4
"""
此题解法：
* 一种就是最朴素的排序概念，拿取第一列，检测是否按字典序，如果不是，就计数器+1，跳到下一列
  如果是字典序再看是否有重复字母，如果没有，就跳出，不用看后面了
  如果有重复字母，就记录重复的位置，继续比较这个位置后面的排序。
  比较的方式还是一样，如果有重复的就还需要记录重复的位置，继续往后比。
  只有最后都按照字典序并且没有重复字母，就可以跳出了。


        self.idx = 0
        items = len(A)
        cols = len(A[0])

        result = 0
        checklist = [list(range(items))]

        while self.idx < cols:
            colchars = []
            for j in checklist:
                colchars.append([A[x][self.idx] for x in j])
            if any([tmp != sorted(tmp) for tmp in colchars]):
                result = result + 1
                self.idx = self.idx + 1
            elif any(len(tmp) != len(set(tmp)) for tmp in colchars):
                tmplist = []
                for jj in checklist:
                    od = {}
                    for j in jj:
                        t = A[j][self.idx]
                        if od.get(t, 0) == 0:
                            od[t] = [j]
                        else:
                            od[t].append(j)
                    tmplist.extend([y for y in od.values() if len(y) >= 2])
                checklist = tmplist[:]
                self.idx = self.idx + 1
            else:
                break
        return result

* 另外一种比较精巧的办法。
1、用一个list（长度是len(A)-1，默认都是False）来记录A[i][index]和A[i+1][index]的排序关系，只有当
   A[i][index]>A[i+1][index] 才能记录成为True
2、每一列数据的依次相邻的两个元素就有3种情况
   I、前序是True 就不看后边了，如果是False 而且 a[i]<a[i+1] 那么就是改为 True
   II、前序是True 就不看后面，如果是False 而且 a[i]==a[i+1] 那么还是False
   III、前序是True就不看后面，如果是False 而且 a[i]>a[i+1] 那么是False 而且 计数器+1
3、利用for else语句
"""
