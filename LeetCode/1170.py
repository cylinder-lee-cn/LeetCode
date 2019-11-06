"""
1170. 比较字符串最小字母出现频次

我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。

例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。

现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，
其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。

示例 1：
输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。

示例 2：
输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。

提示：
1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] 都是小写英文字母
"""

from typing import List
import bisect


class Solution:
    def numSmallerByFrequency(self, queries: List[str],
                              words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))

        wlen = len(words)
        wfs = sorted(map(f, words))

        return [wlen - bisect.bisect(wfs, i) for i in map(f, queries)]


so = Solution()
print(so.numSmallerByFrequency(['cbd'], ['zaaaz']))
print(so.numSmallerByFrequency(["bbb", "cc"], ["a", "aa", "aaa", "aaaa"]))
"""
此题解法：
* 引入二分法查找模块
* 定义一个f函数，统计一个词中最小字母出现的次数
* 计算words的list的长度
* 将words中每个单词利用f计算一次，并将结果排序
* queries中每个单词也利用f计算一次，使用二分法在wfs中查找到对应的索引，用wlen减去索引值就是个数
"""
