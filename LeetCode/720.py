"""
720. 词典中最长的单词
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。
若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

示例 1:
输入:
words = ["w","wo","wor","worl", "world"]
输出: "world"

解释:
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。

示例 2:
输入:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出: "apple"

解释:
"apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。

注意:
所有输入的字符串都只包含小写字母。
words数组长度范围为[1,1000]。
words[i]的长度范围为[1,30]。
"""


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d = {w: len(w) for w in words}
        result = 'z' * 30
        flag = False
        max_len = max(d.values())
        while max_len > 0 and flag is False:
            tmp = [k for k, v in d.items() if v == max_len]
            for m in tmp:
                if all([m[:i] in d for i in range(1, len(m) + 1)]):
                    result = min(result, m)
                    flag = True
                    continue
                else:
                    d[m] = 0
            max_len = max_len - 1
        return result


s = Solution()
print(s.longestWord(["w", "wo", "wor", "world", "worl"]))
print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(
    s.longestWord([
        "yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z",
        "ewq", "yod", "ewqz", "y"
    ]))
"""
此题解法：
* 首先将所有单词进行字数统计后放入字典中，便于查找
* result最大就是30个z
* 初始化最大的单词长度是max(d.values())
* 首先将字典中value是max的都取出来，用all函数来看看依次减掉一个字母是否都在字典中。
  如果在，就和result相比，保留一个最小值,并且标志位说明找到了
* 如果不在，将对应的d[m]置为0，也可以不操作。
* 遍历完后都没有，就将max_len-1，重复上面的操作。

"""
