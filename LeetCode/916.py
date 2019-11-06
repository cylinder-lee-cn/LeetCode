"""
916. 单词子集

我们给出两个单词数组 A 和 B。每个单词都是一串小写字母。

现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称单词 b 是单词 a 的子集。
例如，“wrr” 是 “warrior” 的子集，但不是 “world” 的子集。

如果对 B 中的每一个单词 b，b 都是 a 的子集，那么我们称 A 中的单词 a 是通用的。
你可以按任意顺序以列表形式返回 A 中所有的通用单词。

示例 1：
输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
输出：["facebook","google","leetcode"]

示例 2：
输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
输出：["apple","google","leetcode"]

示例 3：
输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
输出：["facebook","google"]

示例 4：
输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
输出：["google","leetcode"]

示例 5：
输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
输出：["facebook","leetcode"]

提示：
1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] 和 B[i] 只由小写字母组成。
A[i] 中所有的单词都是独一无二的，也就是说不存在 i != j 使得 A[i] == A[j]。
"""


class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        import itertools
        chkset = {}
        result = []

        for b in B:
            newb = sorted(b)
            for k, g in itertools.groupby(newb):
                gl = len(list(g))
                if chkset.get(k, 0) == 0:
                    chkset[k] = gl
                else:
                    chkset[k] = max(gl, chkset[k])

        for a in A:
            if all(a.count(c) >= chkset[c] for c in chkset):
                result.append(a)
        return result


s = Solution()
# print(
#     s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"],
#                   ["e", "o"]))
# print(
#     s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"],
#                   ["l", "e"]))
# print(
#     s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"],
#                   ["e", "oo"]))
# print(
#     s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"],
#                   ["lo", "eo"]))
# print(
#     s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"],
#                   ["ec", "oc", "ceo"]))
print(
    s.wordSubsets(["abbac", "aabac", "bbacb", "aacac", "bcabb"],
                  ['c', 'bc', 'aa']))
print(
    s.wordSubsets(["acaac", "cccbb", "aacbb", "caacc", "bcbbb"],
                  ["cc", "c", "b"]))
print(
    s.wordSubsets([
        "dcbddbbbeb", "edeabaedbc", "beecbdbabe", "bacadddbda", "ecbdebddbb",
        "abeabbcaaa", "eabbdbadbb", "aacabeacde", "bcceeaccae", "ebbdebbcad"
    ], ["add", "b", "ba", "ada", "dcd"]))
"""
此题解法：
* 首先对B进行处理，需要统计每个B中出现的字母以及最大出现次数。
* 可以利用itertools.groupby的来对相同的字符进行分组，获取这个字母以及出现的次数
* 建立一个字典，如果字母不在字典中，那么将key=字母，value=出现次数
* 如果字母在字典中，就比较一下出现次数，将更大的次数更新到字典内
* 最后，遍历A，那么字典里的字母以及出现次数都必须在A中的单词内出现，
  而且A单词统计key字母的次数要>=字典内对应key的次数，就是需要的解
"""
