"""
893. 特殊等价字符串组

你将得到一个字符串数组 A。
如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是特殊等价的。
一次移动包括选择两个索引 i 和 j，且 i％2 == j％2，并且交换 S[j] 和 S [i]。
现在规定，A 中的特殊等价字符串组是 A 的非空子集 S，这样不在 S 中的任何字符串与 S 中的任何字符串都不是特殊等价的。

返回 A 中特殊等价字符串组的数量。

示例 1：
输入：["a","b","c","a","c","c"]
输出：3
解释：3 组 ["a","a"]，["b"]，["c","c","c"]

示例 2：
输入：["aa","bb","ab","ba"]
输出：4
解释：4 组 ["aa"]，["bb"]，["ab"]，["ba"]

示例 3：
输入：["abc","acb","bac","bca","cab","cba"]
输出：3
解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]

示例 4：
输入：["abcd","cdab","adcb","cbad"]
输出：1
解释：1 组 ["abcd","cdab","adcb","cbad"]

提示：
1 <= A.length <= 1000
1 <= A[i].length <= 20
所有 A[i] 都具有相同的长度。
所有 A[i] 都只由小写字母组成。
"""


class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = set()
        for word in A:
            alpha = [0] * 52
            for i, w in enumerate(word):
                alpha[ord(w) - 97 + 26 * (i % 2)] += 1
            count.add(tuple(alpha))

        return len(count)


s = Solution()
print(s.numSpecialEquivGroups(["abcd", "cdab", "adcb", "cbad"]))
print(s.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))
"""
此题解法（来自官网）：

* 关键点：一次移动包括选择两个索引 i 和 j，且 i％2 == j％2，并且交换 S[j] 和 S [i]。
    也就是说字符串上的奇数位的字母集合和偶数位的字母集合是相同的（与顺序无关）。
* 只要是符合上述规则的就是特殊等价字符串
* 如何按照奇数位和偶数位分别统计出现的字母？
    1. 使用字典{0:'a-z',1:'a-z'}，0对应的是偶数位，1对应的是奇数位，但是比较困难，因为要考虑value中值无序。
        在value可以考虑使用set。但是存储成本较高。
    2. 使用数组，利用索引对应关系来进行存放。
        * 建立一个数组[0]*52，index（0-25）对应偶数位的26个字母
                            index（26-51）对应奇数位的26个字母
        * 对应字母进行计数，这样就解决了无序且可以区分奇数位和偶数位的问题。

    3. 将最后的结果使用set排重就知道有多少组特殊等价字符串了。

class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})
-----------------------------------------------------
* 另一种解法：使用排序的操作方式来解决
* 对于List中的每个特殊等价字符串都有：sorted(word[0::2])+sorted(word[1::2])相同。
* 将结果利用set排重即可
* 一句话版本：
return len(set(map(lambda x : "".join(sorted(x[0::2]) + sorted(x[1::2])), A)))

"""
